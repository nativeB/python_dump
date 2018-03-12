import json
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.http import Request


class BrickSetSpider(scrapy.Spider):
    name = "zcrawler"
    with open('serieslinks1.json', 'r') as link:
        links = json.load(link)


    start_urls = links["urls"]
    # start_urls=["http://www.lightdl.xyz/2018/02/ap-bio.html","http://www.lightdl.xyz/2017/04/the-mick.html"]
    def parse(self, response):

        selector1 = '.post-header h1 ::text'
        selector2='.post-timestamp ::text'
        selector3=".post-body div a img ::attr(src) "
        altselector=".post-body .content div div img ::attr(src)"
        altselector2=".post-body  div img ::attr(src)"
        altselector3=".post-body .seperator a img ::attr(src)"
        selector4=".post-body ::text"
        look=None
        if response.css(selector3).extract()!=[]:
            look=response.css(selector3).extract()
        elif response.css(altselector).extract()!=[]:
            look=response.css(altselector).extract()
        elif response.css(altselector2).extract()!=[]:
            look = response.css(altselector2).extract()
        else:look=response.css(altselector3).extract()

        mine=response.css(selector4).extract()
        my=None

        if 'CLICK ON LINKS BELOW TO DOWNLOAD' in mine:
            my=mine.index('CLICK ON LINKS BELOW TO DOWNLOAD')
        elif 'CLICK ON LINKS BELOW TO DOWNLOAD ' in mine:
            my=mine.index('CLICK ON LINKS BELOW TO DOWNLOAD ')
        elif ' CLICK ON LINKS BELOW TO DOWNLOAD' in mine:
            my=mine.index(' CLICK ON LINKS BELOW TO DOWNLOAD' )
        elif ' CLICK ON LINKS BELOW TO DOWNLOAD ' in mine:
           my=mine.index(' CLICK ON LINKS BELOW TO DOWNLOAD ')
        mine=mine[:my]
        # rpint("title :",response.css(selector1).extract())

        links = LinkExtractor(allow=('mkv$|MKV$|mp4$|MP4$|avi$|AVI$|webm$|WEBM$'),restrict_css=('.post-body')).extract_links(response)
        final_link={}
        for link in links:
            final_link[link.text]=link.url
        yield {
            "name":response.css(selector1).extract(),
            "date":response.css(selector2).extract(),
            "image_urls":look,
            "about":mine,
            "link":final_link,


        }

