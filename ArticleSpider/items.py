import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )

    def get_insert_sql(self):
        insert_sql = """
            insert into jobbole_article
            VALUES (%s,%s)
        """
        params = (self["title"], self["fav_nums"])

        return insert_sql, params
