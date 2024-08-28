from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Finviz_scrape.spiders.finviz import Scrape_Spider


process = CrawlerProcess(get_project_settings())
# Add a spider to the process
process.crawl(Scrape_Spider)
# Start the crawling process
process.start()