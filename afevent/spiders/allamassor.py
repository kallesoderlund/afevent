import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from scrapy.crawler     		import CrawlerProcess
from urlparse 					import urljoin

class MySpider(CrawlSpider):
	name 		= "allamassor"
	allowed_domains	= ["allamassor.se"]
	start_urls	= ["http://www.allamassor.se/kalender?q=1&qa=49", "http://www.allamassor.se/kalender?q=1&qa=38", "http://www.allamassor.se/kalender?q=1&qa=30", "http://www.allamassor.se/kalender?q=1&qa=39", "http://www.allamassor.se/kalender?q=1&qa=55", "http://www.allamassor.se/kalender?q=1&qa=21", "http://www.allamassor.se/kalender?q=1&qa=23", "http://www.allamassor.se/kalender?q=1&qa=27", "http://www.allamassor.se/kalender?q=1&qa=56"]
 
	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('/html/body/div[4]/div[1]/div[2]/div/a')), callback="parse", follow = True),
	)

	def parse(self, response):
		i = 0
		for div in response.xpath('//div[@class="exhibit clearfix"]'):
			item = AfeventItem()
	#Store data into lists
			item['title'] = div.xpath('//a/div/div[@class="header"]/text()').extract()[i]
			url = div.xpath('.//a[@href]/@href').extract()[0]
			url = 'http://allamassor.se/' + url
			item['url'] = url

	#Remove unwanted characters
			location = div.xpath('//span[@class="ort"]/text()').extract()[i]
			for char in " | ":
				location = location.replace(char, "")
				item['location'] = location

	#The following code changes the format of the date
			origDate = div.xpath ('//span[@class="date"]/text()').extract()[i]
			#split up the text in the date
			newDate = origDate.split()

	#Handles if date is between two dates, e.g. "10 - 11 maj 2016"
			if len(newDate) > 3:
				rightDate = []
				rightDate.extend((newDate[0], newDate[3], newDate[4]))
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

			if i < len(response.xpath('//div[@class="exhibit clearfix"]')):
			 	i = i + 1
			 	yield request

	#For items collected in sites where the spider follows a url to another site
	def parse_second(self, response):
		item = response.meta['item']
		item ['description'] = ''.join(response.xpath('//div[@class="bigdescription"]/text()').extract())
		item['host'] = ''.join(response.xpath('//tr[@class="organizer"]/td[@class="detail"]/a/text()').extract())
		item['time'] = ''.join(response.xpath('//tr[@class="time"]/td[@class="detail"]/text()').extract())
		yield item


		





