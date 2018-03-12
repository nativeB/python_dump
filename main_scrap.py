import json
import scrapy

from scrapy.http import Request


class BrickSetSpider(scrapy.Spider):
    name = "zcrawler"
    with open('../../series_links.json', 'r') as link:
        links = json.load(link)


    start_urls = links["links"]

    def parse(self, response):

        selector1 = '.post-header h1'


