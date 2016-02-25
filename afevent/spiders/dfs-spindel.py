# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spiders 		import Spider
from scrapy.selector 		import HtmlXPathSelector
from afevent.items		import AfeventItem
from scrapy.http		import Request
from scrapy.crawler             import CrawlerProcess
 
class MySpider(Spider):
	name 		= "dfs"
	allowed_domains	= ["natverk.dfs.se"]
	start_urls	= ["https://natverk.dfs.se/pagang"]
 
	def parse(self, response):
		divs    = response.xpath('//tbody')

		for div in divs:
                    item = AfeventItem()
                    item['title']   = div.xpath('./tr/td/div[@class = "event-title"]/span[@class = "link"]/text()').extract()
                    item['city']    = div.xpath('./tr/td[4]/text()').extract()
                    item['host']    = div.xpath('./tr/td[5]/a/text()').extract()
                    item['date']    = div.xpath('./tr/td[1]/span/text()').extract()
                    item['link']    = div.xpath('./tr/td[3]/div[2]/a/@href').extract()

                    
                    #Removes '\n' and ' ' from city, and adds part of url to link
                    item['city'] = [x.strip('\n') for x in item['city']]
                    item['city'] = [x.strip(' ') for x in item['city']]
                    item['link'] = ['https://natverk.dfs.se' + x for x in item['link']]
                    item['time'] = [x.split(' ') for x in item['date']]

                yield item

##process = CrawlerProcess()
##process.crawl(dfs)
##process.start()
