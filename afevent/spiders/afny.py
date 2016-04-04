import scrapy
from scrapy.spiders 					import CrawlSpider, Rule
from scrapy.selector 					import HtmlXPathSelector
from scrapy.linkextractors				import LinkExtractor
from afevent.items						import AfeventItem
from scrapy.http						import Request
from scrapy.contrib.spiders 			import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class myItems(scrapy.Item):
	title 		= scrapy.Field()
	city 		= scrapy.Field()
	venue 		= scrapy.Field()
	date 		= scrapy.Field()
	time 		= scrapy.Field()
	description = scrapy.Field()
	host 		= scrapy.Field()
	url 		= scrapy.Field()
	long_description = scrapy.Field()

class MySpider(CrawlSpider):
	name 		= "afny"
	allowed_domains	= ["afconsult.com"]
	start_urls	= ["http://www.afconsult.com/sv/jobba-hos-oss/event-seminarier--massor/"]
	rules = (Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="CalendarContainer"]/div/div/a')), callback="parser", follow = True),
	)

	def parser(self, response):
		divs = response.xpath('//body')
		item = myItems()

		title_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/h1/text()').extract())
		date_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/span/text()').extract())
		time_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[2]/span[2]/span/text()|//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[3]/span/text()[3]').extract())
		url_list = ''.join(divs.xpath('//*[@id="mainContent"]/section/div/div/nav/ul/li[4]/a/@href').extract())
		url_list = 'http://www.afconsult.com' + url_list
		description_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article//text()').extract())

		
		item['title'] = title_list
		item['url'] = url_list
		item['date'] = date_list
		item['time'] = time_list
		item['description'] = description_list

		yield item

