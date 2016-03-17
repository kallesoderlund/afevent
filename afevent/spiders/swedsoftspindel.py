import scrapy
from scrapy.spiders 	import Spider
from scrapy.selector 	import HtmlXPathSelector
from afevent.items		import AfeventItem
from scrapy.http		import Request
from scrapy.crawler     import CrawlerProcess

class myItems(scrapy.Item):
	title = scrapy.Field()
	city = scrapy.Field()
	venue = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	description = scrapy.Field()
	host = scrapy.Field()
	url = scrapy.Field()

class MySpider(Spider):
	name 		= "swedint"
	allowed_domains	= ["swedsoft.se"]
	start_urls	= ["http://swedsoft.se/kalender/kalendarium/"]
 
	def parse(self, response):
		divs    = response.xpath('//body')
		item = myItems()

		#Store data into lists
		title_list = divs.xpath('//*[@class ="h2 entry-title"]/text()').extract()
		city_list = divs.xpath('//*[@id]/div[3]/h2/text()').extract()
		venue_list = divs.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()[1]').extract()
		date_list = divs.xpath ('//*[@id]/div[3]/p/text()').extract()
		time_list = divs.xpath('//*[@id]/div[3]/table/tr[2]/td[2]/text()').extract()
		description_list = divs.xpath('//*[@id]/div[2]/section/p/text()').extract()
		url_list = divs.xpath('//*[@id="main"]/div/div/a/@href').extract()
		

	

		#Combine related attributes into events
		for x in range(0,len(title_list)):
			item['title'] = title_list[x]
			item['city'] = city_list[x]
			item['venue'] = venue_list[x]
			item['date'] = date_list[x]
			item['url'] = url_list[x]
			#item['time'] = time_list[x]
			item['description'] = description_list[x]
			item['host'] = 'Swedsoft'
			yield item

