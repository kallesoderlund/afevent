import scrapy
from scrapy.spiders 					import CrawlSpider, Rule
from scrapy.selector 					import HtmlXPathSelector
from scrapy.linkextractors				import LinkExtractor
from afevent.items						import AfeventItem
from scrapy.http						import Request
from scrapy.contrib.spiders 			import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class MySpider(CrawlSpider):
	name 		= "swedext"
	allowed_domains	= ["swedsoft.se"]
	start_urls	= ["http://swedsoft.se/kalender/andra-event/"]
 	rules = (Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="main"]/div/div/a')), callback="parse", follow = True),
	)
	def parse(self, response):
		i = 0
		for div in response.xpath('//div[@class="article-content"]'):
			item = AfeventItem()
			item['title'] = div.xpath('//h1[@class="h2 entry-title"]/text()').extract()[i]
			item['location'] = div.xpath('//*[@id]/div[3]/h2/text()').extract()[i]
			item['venue'] = div.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()').extract()[i]
			origDate = div.xpath('//*[@id]/div[3]/p/text()').extract()[i]

			#split up the text in the date
			newDate = origDate.split()

			#handles if date is between two dates, e.g. "10 - 11 maj 2016"
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

			item['url'] = div.xpath('//*[@id="main"]/div/div/a/@href').extract()[i]
			follow_url_1 = div.xpath('//*[@id="main"]/div/div/a/@href').extract()[i]
			follow_url = 'http://swedsoft.se/event-ovrigt/' + follow_url_1
			request = Request(follow_url, callback = self.parse_url)
			request.meta['item'] = item

			if i < len(response.xpath('//div[@class="article-content"]')):
				i = i + 1	
			yield request

	def parse_url(self, response):
 		item = response.meta['item']
 		item['description'] = ''.join(response.xpath('//*[@id]/section/p/text() | //*[@id]/section/p/strong/text()').extract())

 		yield item
		


