from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl('lanyrd', domain='lanyrd.com')
process.crawl('dfs', domain='natverk.dfs.se')
process.crawl('swedext', domain='swedsoft.se')
process.crawl('swedint', domain='swedsoft.se')
process.crawl('afny', domain='afconsult.com')
process.crawl('allamassor', domain='allamassor.se')
process.crawl('stimdi', domain='stimdi.se')
process.crawl('iva', domain='iva.se')
process.start()