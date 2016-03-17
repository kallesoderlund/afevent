import scrapy
from scrapy.spiders 	import Spider
from scrapy.selector 	import HtmlXPathSelector
from afevent.items		import AfeventItem
from scrapy.http		import Request
from scrapy.crawler     import CrawlerProcess
from scrapy.loader 		import ItemLoader

# from scrapy.contrib.loader 				import ItemLoader
# from scrapy.contrib.loader.processor	import TakeFirst, MapCompose, Join

class myItems(scrapy.Item):
	title = scrapy.Field()
	city = scrapy.Field()
	venue = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	description = scrapy.Field()
	url = scrapy.Field()

class MySpider(Spider):
	name 		= "swedext"
	allowed_domains	= ["swedsoft.se"]
	start_urls	= ["http://swedsoft.se/kalender/andra-event/"]
 
	def parse(self, response):
		divs    = response.xpath('//body')
		item = myItems()

		#Store data into lists
		title_list = divs.xpath('//h1[@class="h2 entry-title"]/text()').extract()

		#Since the city tag sometimes is empty:
		city_list = []
		for h2 in divs.xpath('//h2'):
			city = ''.join(h2.xpath('.//text()').extract())
			city_list.append(city)

		venue_list = divs.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()').extract()
		date_list = divs.xpath ('//*[@id]/div[3]/p/text()').extract()
		description_list = divs.xpath('//*[@id]/div[2]/section/p/text()').extract()
		url_list = divs.xpath('//*[@id="main"]/div/div/a/@href').extract()
		

		#Combine related attributes into events
		for x in range(0,len(title_list)):
			item['title'] = title_list[x]
			item['city'] = city_list[x]
			item['url'] = url_list[x]
			#item['venue'] = venue_list[x]
			item['date'] = date_list[x]
			#item['description'] = description_list[x]
			yield item


