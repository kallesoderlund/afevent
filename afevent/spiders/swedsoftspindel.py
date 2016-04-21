import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from scrapy.crawler     		import CrawlerProcess
from urlparse 					import urljoin


class MySpider(CrawlSpider):
	name 		= "swedint"
	allowed_domains	= ["swedsoft.se"]
	start_urls	= ["http://swedsoft.se/kalender/kalendarium/"]
 
	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="main"]/div/div/')), callback="parse", follow = True),
	)

	def parse(self, response):
		i = 0
		
		for div in response.xpath('//*[@id="main"]/div/div/a'):
			item = AfeventItem()
		
		#Store data into lists
			item['title'] = div.xpath('//*[@class ="h2 entry-title"]/text()').extract()[i]
			item['location'] = div.xpath('//*[@id]/div[3]/h2/text()').extract()[i]
			item['venue'] = div.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()[1]').extract()[i]
			#the following code changes the format of the date
			origDate = div.xpath ('//*[@id]/div[3]/p/text()').extract()[i]
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

			item['host'] = "Swedsoft"
			item['description'] = div.xpath('//*[@id]/div[2]/section/p/text()').extract()[i]
			item['url'] = div.xpath('//*[@id="main"]/div/div/a/@href').extract()[i]
			follow_url = div.xpath('//*[@id="main"]/div/div/a/@href').extract()[i]
			request = Request(follow_url, callback = self.parse_second)
			request.meta['item'] = item
		
			if i < len(response.xpath('//*[@id="main"]/div/div/a')):
				i = i + 1		
			yield request


	def parse_second(self, response):
		item = response.meta['item']
		item ['description'] = ''.join(response.xpath('//*[@id]/section/p//text()|//*[@id]/section/p//text()|//*[@id]/section/p//text()').extract())
		yield item

