from twisted.internet import asyncioreactor
asyncioreactor.install()
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from newsspider.spiders.trends_news import TrendsNewsSpider


def run_spider(country):
    process = CrawlerProcess(get_project_settings())
    process.crawl(TrendsNewsSpider, country=country)
    process.start()

if __name__ == '__main__':
    country = "tunisia"
    run_spider(country)
