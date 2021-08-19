import datetime
import scrapy
from gazette.spiders.base import BaseGazetteSpider

class SpPauliniaSpider(BaseGazetteSpider):
    name = "sp_paulinia"
    TERRITORY_ID = "2905206"
    start_date = datetime.date(2010, 1, 4)
    allowed_domains = ["www.paulinia.sp.gov.br/"]
    start_urls = ["http://www.paulinia.sp.gov.br/semanarios/"]

    def parse(self, response):
        yield {
            “date”: datetime.date.today(),
            “file_urls”: [response.url],
        }