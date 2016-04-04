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
			item['city'] = div.xpath('//*[@id]/div[3]/h2/text()').extract_first()
			item['venue'] = div.xpath('//*[@id]/div[3]/table/tr[1]/td[2]/text()').extract()[i]
			item['date'] = div.xpath('//*[@id]/div[3]/p/text()').extract()[i]
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
		


