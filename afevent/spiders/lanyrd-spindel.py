import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from urlparse 					import urljoin

class MySpider(CrawlSpider):
	name		= "lanyrd"
	allowed_domains	= ["lanyrd.com"]
	start_urls	= ["http://lanyrd.com/places/sweden/"]

	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="conference-listing"]/div/div[2]/ol/li/h4/a')), callback="parse", follow = True),
	)

	def parse(self, response):
		i = 0
		#url_list = []

		for div in response.xpath('//li[@class="conference vevent"]'):
			item = AfeventItem()
			item['city'] = div.xpath('.//p[@class="location"]/a[3]/text()').extract_first()
			item['title'] = div.xpath('//h4/a/text()').extract()[i]
			item['date'] = div.xpath('//p[@class="date"]/abbr[1]/@title').extract()[i]
			item['host'] = ''
			item['time'] = ''
			
			follow_url_1 = div.xpath('//h4/a/@href').extract()[i]
			follow_url = 'http://lanyrd.com' + follow_url_1
			request = Request(follow_url, callback = self.parse_url)
			request.meta['item'] = item

			if i < len(response.xpath('//li[@class="conference vevent"]')):
				i = i + 1	
			yield request

 	def parse_url(self, response):
 		item = response.meta['item']
 		
 		link = response.xpath('//*[@class="split first item-meta"]/ul/li/a').extract()
 		item['url'] = response.xpath('/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/@href').extract()[0]
 		yield item


