__author__ = 'github.com/dssalaza'

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Article(Item):
    article = Field()
    id = Field()


class WebSpider(Spider):
    name = "NoboaSpider"
    start_urls = ['http://www.alvaronoboa.com/']

    def parse(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@id="content"]/div/article')
        for i, elem in enumerate(articles):
            item = ItemLoader(Article(), elem)
            item.add_value('id', i)
            item.add_xpath('article', './/header/h2/a/text()')
            yield item.load_item()