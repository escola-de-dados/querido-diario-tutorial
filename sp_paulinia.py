#  source ../../../.venv/bin/activate
#  scrapy crawl sp_paulinia

import datetime

import scrapy

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia_v2"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["www.paulinia.sp.gov.br"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios"]

    def parse(self, response):
        years = response.css("div.col-md-1")

        for year in years:
            year_to_scrape = int(year.xpath("./a/font/text()").get())

            # Para não fazer requisições desnecessárias, se o ano já for o da página
            # inicial (página inicial é o ano atual) ou então for anterior ao ano da
            # data inicial da busca, não iremos fazer a requisição
            if (
                year_to_scrape < self.start_date.year
                or year_to_scrape == datetime.date.today().year
            ):
                continue

            # Com Scrapy é possível utilizar regex direto no elemento com os métodos
            # `.re` e `.re_first` (na maioria das vezes é suficiente e não precisamos
            # usar métodos da biblioteca `re`)
            event_target = year.xpath("./a/@href").re_first(r"(ctl00.*?)',")

            # O método `.from_response` nesse caso é bem útil pois pega vários
            # elementos do tipo <input> que já estão dentro do elemento <form>
            # localizado na página e preenche eles automaticamente no formdata, assim
            # é possível economizar muitas linhas de código
            yield scrapy.FormRequest.from_response(
                response,
                formdata={"__EVENTTARGET": event_target},
                callback=self.parse_year,
            )

        # O `yield from` permite fazermos `yield` em cada resultado do método gerador
        # `self.parse_year`, assim, aqui estamos dando `yield` em todos os itens
        # `Gazette` raspados da página inicial
        yield from self.parse_year(response)

    def parse_year(self, response):
        editions = response.xpath(
            "//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]"
        )

        for edition in editions:
            document_href = edition.xpath("./@href").get()

            title = edition.xpath("./text()")

            gazette_date = datetime.datetime.strptime(
                title.re_first(r"\d{2}/\d{2}/\d{4}"), "%d/%m/%Y"
            ).date()
            edition_number = title.re_first(r"- (\d+) -")
            is_extra_edition = "extra" in title.get().lower()

            # Esse site "esconde" o link direto do PDF por trás de uma série de
            # redirecionamentos, porém, como nas configurações do projeto é permitido
            # que arquivos baixados sofram redirecionamento, é possível colocar o link
            # "falso" já no item `Gazette` e o projeto vai conseguir baixar o documento
            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[response.urljoin(document_href)],
                is_extra_edition=is_extra_edition,
                power="executive",
            )
