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
            yield Request(url=parse.urljoin(response.url, post_url),
                          callback=self.parse_detail)

            # 提取下一页并交给scrapy进行下载
            # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
            # if next_url:
            #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        yield item_loader.load_item()
