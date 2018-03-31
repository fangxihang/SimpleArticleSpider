import scrapy

from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import JobBoleArticleItem, ArticleItemLoader


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            post_url = post_node.css("::attr(href)").extract_first("")
            image_url = post_node.css("img::attr(src)").extract_first("")

            yield Request(url=parse.urljoin(response.url, post_url),meta={"front_image_url":image_url},
                          callback=self.parse_detail)

    def parse_detail(self, response):
        front_image_url = response.meta.get("front_image_url", "")
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("front_image_url", [front_image_url])
        yield item_loader.load_item()
