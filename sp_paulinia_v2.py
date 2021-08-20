
import datetime
# import scrapy
from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["paulinia.sp.gov.br"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios/"]

    def parse(self, response):
        editions = response.xpath(
            "//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]"
        )
        for edition in editions:
            import pdb; pdb.set_trace()
            final_url = edition.xpath("./@href").get()
            link = "http://www.paulinia.sp.gov.br/semanarios/" + final_url
            # description = edition.xpath(
            #     "./text()"
            # ).get()
            # isso retorna string como "29/01/2021 - 1582 - Edição Normal" - falta ainda separar cada info

            yield Gazette(
                # edition_number = ,
                file_urls=[link],
                power="executive",
            )

