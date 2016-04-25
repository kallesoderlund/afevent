# import scrapy
# from scrapy.spiders 					import CrawlSpider, Rule
# from scrapy.selector 					import HtmlXPathSelector
# from scrapy.linkextractors				import LinkExtractor
# from afevent.items						import AfeventItem
# from scrapy.http						import Request
# from scrapy.contrib.spiders 			import CrawlSpider, Rule
# from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from scrapy.crawler     		import CrawlerProcess
from urlparse 					import urljoin

class MySpider(CrawlSpider):
	name 		= "af"
	allowed_domains	= ["afconsult.com"]
	start_urls	= ["http://www.afconsult.com/sv/jobba-hos-oss/event-seminarier--massor/"]
	rules = (Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="CalendarContainer"]/div')), callback="parser", follow = True),
	)

	def parser(self, response): 
		i = 0
		for div in response.xpath('//*[@id="CalendarContainer"]/div/div/a'):
			item = AfeventItem()
			print "response.xpath"
			item['title'] = div.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/h1/text()').extract()[i]
			item['venue'] = div.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[2]/text()').extract()[i]
			item['date'] = div.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/span/text()').extract()[i]
			item['time'] = div.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[2]/span[2]/span/text()|//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[3]/span/text()[3]').extract()[i]
			item['url'] = div.xpath('//*[@id="mainContent"]/section/div/div/nav/ul/li[4]/a/@href').extract()[i]
			follow_url_1 = div.xpath('//*[@id="mainContent"]/section/div/div/nav/ul/li[4]/a/@href').extract()[i]
			follow_url = 'http://www.afconsult.com' + follow_url_1
			request = Request(follow_url, callback = self.parse_url)
			request.meta['item'] = item

			if i < len(response.xpath('//*[@id="CalendarContainer"]/div/div/a')):
				i = i + 1	
				print i
			yield request

	def parse_url(self, response):
 		item = response.meta['item']
 		item['description'] = ''.join(response.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article//text()').extract())
 		print "parse_url"
 		yield item



		# divs = response.xpath('//body')
		# item = myItems()

		# title_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/h1/text()').extract())
		# date_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/span/text()').extract())
		# time_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[2]/span[2]/span/text()|//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[3]/span/text()[3]').extract())
		# url_list = ''.join(divs.xpath('//*[@id="mainContent"]/section/div/div/nav/ul/li[4]/a/@href').extract())
		# url_list = 'http://www.afconsult.com' + url_list
		# description_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article//text()').extract())
		# venue_list = ''.join(divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[2]/text()[]').extract())


		# item['title'] = title_list
		# item['url'] = url_list
		# item['date'] = date_list
		# item['time'] = time_list
		# item['description'] = description_list
		# item['venue'] = venue_list
		#item['long_description'] = long_description_list

		#yield item

