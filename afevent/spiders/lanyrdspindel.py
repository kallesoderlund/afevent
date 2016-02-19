# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spiders 		import Spider
from scrapy.selector 		import HtmlXPathSelector
from afevent.items		import AfeventItem
from scrapy.http		import Request
 
class MySpider(Spider):
	name 		= "lanyrd"
	allowed_domains	= ["lanyrd.com"]
	start_urls	= ["http://lanyrd.com/places/sweden/"]
 
	def parse(self, response):
		divs    = response.xpath('//li')
		items   = []

		for div in divs:
                    item = AfeventItem()
                    item['title'] = div.xpath('//*[@id="conference-listing"]/div/div[2]/ol/li/h4/a/text()').extract()
                    item['city'] = div.xpath('//*[@id="conference-listing"]/div/div[2]/ol/li/p[1]/a[3]/text()').extract()
                    item['date'] = div.xpath('//*[@id="conference-listing"]/div/div[2]/ol/li/p[2]/abbr[2]/text()').extract()

                yield item

               
