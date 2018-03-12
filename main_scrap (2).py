import scrapy

class ProductSpider(scrapy.Spider):
    name = "zcrawler"
    with open('../series_links.json', 'r') as link:
        links = json.load(link)
    start_urls = links['url']



    def parse(self, response):
        selector = ".post .entry h3 a ::attr(href)"
        mine = response.css(selector).extract()
        yield {

            "links": mine,

        }


