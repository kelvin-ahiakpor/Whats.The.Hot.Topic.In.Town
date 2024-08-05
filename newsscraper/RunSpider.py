import asyncio
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from newsspider.spiders.news_scraper import TrendsNewsSpider

def run_spider(country):
    process = CrawlerProcess(get_project_settings())
    process.crawl(TrendsNewsSpider, country=country)
    process.start()

if __name__ == "__main__":
    import sys
    country = sys.argv[1]
    run_spider(country)