import scrapy


class DivansSpiderSpider(scrapy.Spider):
    name = "divans_spider"
    allowed_domains = ["divan.ru", "www.divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        pass
