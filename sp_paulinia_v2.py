#  source ../../../.venv/bin/activate
#  scrapy crawl sp_paulinia

import datetime

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider

# import scrapy


class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["www.paulinia.sp.gov.br/"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios"]
    # handle_httpstatus_list = [301]

    def parse(self, response):
        # years = response.xpath('//a[starts-with(@id,"corpo_lnkItem")]')
        # for year in years:
        # link = print(year.xpath("./@href").get())
        # current_year = xpath("//font/text()").get()).get()
        # import pdb; pdb.set_trace()

        editions = response.xpath(
            "//div[@class='container body-content']//div[@class='row']//a[contains(@href, 'AbreSemanario')]"
        )
        for edition in editions:
            final_url = edition.xpath("./@href").get()
            link_pdf = "www.paulinia.sp.gov.br/semanarios/" + final_url

            # Vamos separar as três informações da string "29/01/2021 - 1582 - Edição Normal"
            full_desc = edition.xpath("./text()").get()
            sep = " - "
            gazette_date = datetime.datetime.strptime(
                full_desc.split(sep)[0], "%d/%m/%Y"
            ).date()
            edition_number = full_desc.split(sep)[1]
            is_extra_edition = full_desc.split(sep)[2].strip() == "Edição Extra"

            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[link_pdf],
                is_extra_edition=is_extra_edition, 
                power="executive",
            )
