import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class ArticleItemLoader(ItemLoader):
    pass


class JobBoleArticleItem(scrapy.Item):
    front_image_url = scrapy.Field()
    title = scrapy.Field()