import scrapy

from scrapy.http import Request


class BrickSetSpider(scrapy.Spider):
    name = "zcrawler"
    start_urls = ['http://lightdl.xyz','http://www.lightdl.xyz/2018/02/ap-bio.html']

    def parse(self, response):

        selector1 = '#Label2 div ul li a ::attr(href)'


        # for brickset in response.css(SET_SELECTOR):
        #     label = 'div ul li a ::attr(href)'
        #     link='div ul li a ::text'
        #
        #     yield {
        #         'name': brickset.css(label).extract(),
        #         'link':brickset.css(link).extract(),
        #
        #     }

        print('lighter',response.css(selector1).extract())



    # def parse_labels(self, response):
    #     SET_SELECTORs = '.entry h3 a::attr(href)'
    #
    #
    #     yield { 'name':  response.css(SET_SELECTORs).extract()}
    #
