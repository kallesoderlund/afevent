import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from scrapy.crawler     		import CrawlerProcess
from urlparse 					import urljoin

class MySpider(CrawlSpider):
	name 		= "iva"
	allowed_domains	= ["iva.se"]
	start_urls	= ["http://www.iva.se/kommande-event/"]
 
	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('/html/body/main/div/div/article/div/div/div[1]/div[1]/a')), callback="parse", follow = True),
	)

	def parse(self, response):
		i = 0
		for div in response.xpath('//article'):
			item = AfeventItem()
	#Store data into lists
			item['title'] = div.xpath('//div/div/div[1]/div[1]/a/*[self::h1 or self::h2]/text()').extract()[i]
			url = div.xpath('.//div/div/div[1]/div[1]/a/@href').extract()[0]
			url = 'http://iva.se' + url
			item['url'] = url
			item['description'] = div.xpath('//div/div/div[1]/div[2]/figure/div/p/text()').extract()[i]

	#Remove unwanted characters
			location = div.xpath('//div/div/div[2]/section/ul/li[@class="schedule-where icon-where schedule__row"]/text()').extract()[i]
			item['location'] = location.strip()

	#The following code changes the format of the date
			origDate = div.xpath ('//div/div/div[2]/section/ul/li[@class="schedule-when icon-when schedule__row"]/text()').extract()[i]
			#split up the text in the date
			newDate = origDate.split()

	#Handles if date is between two dates, e.g. "10 - 11 maj 2016"
			if len(newDate) > 3:
				rightDate = []
				rightDate.extend((newDate[2], newDate[3], newDate[4]))

				newDate = rightDate

	#Assign values to month names
			month = ["", "januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"].index(newDate[1])

	#Assign a "0" in the beginning if month number is < 10
			if month < 10:
				zeroMonth = [0, month]
				zeroMonth = ''.join(map(str, zeroMonth))
			else:
				zeroMonth = month

	#same thing as above with day
			if int(newDate[0]) < 10:
				zeroDate = [0, newDate[0]]
				zeroDate = ''.join(map(str, zeroDate))
			else:
				zeroDate = newDate[0]

	#Puts everything together and stores into item['date']
			finalDate = [newDate[2], zeroMonth, zeroDate]
			item['date'] = '-'.join(finalDate)
			request = Request(url, callback = self.parse_second)
			request.meta['item'] = item

			if i < len(response.xpath('//article[@class="item"]')):
			 	i = i + 1
			 	yield request

			yield item



	def parse_second(self, response):
	#	item = response.meta['item']
	#	item ['description'] = ''.join(response.xpath('//div[@class="bigdescription"]/text()').extract())
	#	item['host'] = ''.join(response.xpath('//tr[@class="organizer"]/td[@class="detail"]/a/text()').extract())
	#	item['time'] = ''.join(response.xpath('//tr[@class="time"]/td[@class="detail"]/text()').extract())
		yield self
		