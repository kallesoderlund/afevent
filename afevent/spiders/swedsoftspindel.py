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
			item['city'] = div.xpath('//*[@id]/div[3]/h2/text()').extract()[i]
			item['venue'] = div.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()[1]').extract()[i]
			item['date'] = div.xpath ('//*[@id]/div[3]/p/text()').extract()[i]
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

	

		#Combine related attributes into events
		for x in range(0,len(title_list)):
			item['title'] = title_list[x]
			item['city'] = city_list[x]
			item['venue'] = venue_list[x]
			item['date'] = date_list[x]
			item['url'] = url_list[x]
			item['host'] = ''
			#item['time'] = time_list[x]
			item['description'] = description_list[x]
			item['host'] = 'Swedsoft'
			yield item

