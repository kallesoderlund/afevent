import scrapy
from scrapy.spiders 		import CrawlSpider, Rule
from scrapy.selector 		import HtmlXPathSelector
from scrapy.linkextractors	import LinkExtractor
from afevent.items			import AfeventItem
from scrapy.http			import Request
from urlparse 				import urljoin

class MySpider(CrawlSpider):
	name		= "lanyrd"
	allowed_domains	= ["lanyrd.com"]
	start_urls	= ["http://lanyrd.com/places/sweden/"]

	rules = (
		Rule(LinkExtractor(allow = (), restrict_xpaths=('//*[@id="conference-listing"]/div/div[2]/ol/li/h4/a')), callback="parse", follow = True),
	)
 
	def parse(self, response):
		i = 0
		url_list = []

		for div in response.xpath('//li[@class="conference vevent"]'):
			item = AfeventItem()
			item['city'] = div.xpath('.//p[@class="location"]/a[3]/text()').extract_first()
			item['title'] = div.xpath('//h4/a/text()').extract()[i]
			item['date'] = div.xpath('//p[@class="date"]/abbr[1]/@title').extract()[i]
			item['host'] = ''
			item['time'] = ''
			item['url'] = div.xpath('//h4/a/@href').extract()[i]
			item['url'] = 'http://lanyrd.com' + item['url']
			# request = Request(url_list[i], callback = self.parse_url)
			# request.meta['item'] = item

			if i < len(response.xpath('//li[@class="conference vevent"]')):
				i = i + 1	
			yield item
			#yield request

 	# def parse_url(self, response):
 	# 	item = response.meta['item']
 	# 	hxs = HtmlXPathSelector(response)
 	# 	link = hxs.select('//*[@class="split first item-meta"]/ul/li/a').extract()
 	# 	item['url'] = hxs.select('/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/span/text()').extract()[0]
 	# 	yield item
		# for title, city, date, link in zip(title_list, city_list, date_list, link_list):
		# 	item = AfeventItem()
		# 	item['title'] = title
		# 	item['city'] = city
		# 	item['date'] = date
		# 	request = Request(link_list, callback = self.parse_url)
		# 	requst.meta['item'] = item
		# 	yield request

		#yield item

              
		# for x in range(0, len(title_list)):
		# 	item = AfeventItem()
		# 	item['title'] = title_list[x]
		# 	item['city'] = city_list[x]
		# 	item['date'] = date_list[x]
		# 	request = Request(link_list[x], callback = self.parse_url)
		# 	request.meta['item'] = item
		#yield request


