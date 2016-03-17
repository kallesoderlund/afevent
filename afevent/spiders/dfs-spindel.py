import scrapy
from scrapy.spiders 	import Spider
from scrapy.selector 	import HtmlXPathSelector
from afevent.items		import AfeventItem
from scrapy.http		import Request
from scrapy.crawler     import CrawlerProcess

class myItems(scrapy.Item):
	title = scrapy.Field()
	city = scrapy.Field()
	host = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	url = scrapy.Field()


class MySpider(Spider):
	name 		= "afevent"
	allowed_domains	= ["natverk.dfs.se"]
	start_urls	= ["https://natverk.dfs.se/pagang"]
 
	def parse(self, response):
		divs    = response.xpath('//tbody')
		item = myItems()

		#Store data into lists
		title_list = divs.xpath('./tr/td/div[@class = "event-title"]/span[@class = "link"]/text()').extract()
		city_list = divs.xpath('./tr/td[4]/text()').extract()
		host_list = divs.xpath('./tr/td[5]/a/text()').extract()
		date_time_list = divs.xpath('./tr/td[1]/span/text()').extract()
		url_list = divs.xpath('./tr/td[3]/div[2]/a/@href').extract()

		#Trim the data
		city_list = [y.strip() for y in city_list]
		date_time_list = [y.split(' ') for y in date_time_list]
		date_list, time_list = map(list, zip(*date_time_list))
		url_list = ['https://natverk.dfs.se' + y for y in url_list]

		#Combine related attributes into events
		for x in range(0,len(title_list)):
			item['title'] = title_list[x]
			item['city'] = city_list[x]
			item['host'] = host_list[x]
			item['date'] = date_list[x]
			item['time'] = time_list[x]
			item['url'] = url_list[x]
			
			yield item
		
