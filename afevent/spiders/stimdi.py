import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from scrapy.crawler     		import CrawlerProcess
from urlparse 					import urljoin

class MySpider(CrawlSpider):
	name 		= "stimdi"
	allowed_domains	= ["stimdi.se"]
	start_urls	= ["http://www.stimdi.se/tidslinjen/"]
 
	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="content"]/div/div/h2/a')), callback="parse", follow = True),
	)

	def parse(self, response):
		i = 0
		print i
		for div in response.xpath('//*[@id="content"]/div/div'):
			print "IN FOR"
			item = AfeventItem()
	#Store data into lists
			item['title'] = div.xpath('//h2/a/text()').extract()[i]
			item['url'] = div.xpath('//h2/a/@href').extract()[i]
			item['location'] = ''
			item['description'] = div.xpath('//*[@id="content"]/div/div[1]/a[1]/p/text()').extract()[i]

	#The following code changes the format of the date
			origDate = div.xpath ('//p/text()').extract()[i]
			newDate = ''.join(origDate).replace(',', '').split()
			
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
			print i

	 		if i < len(response.xpath('//*[@id="content"]/div/div')):
	 			print "I IF"
	 			print len(response.xpath('//*[@id="content"]/div/div'))
	 		 	i = i + 1

	 		yield item


	



		





