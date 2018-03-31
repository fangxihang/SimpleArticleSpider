# -*- coding: utf-8 -*-



import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


# def get_insert_sql(self):
#     insert_sql = """
#         insert into jobbole_article(title)
#         VALUES (%s)
#     """
#     params = (self["title"])
#
#     return insert_sql, params


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
