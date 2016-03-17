# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.spiders 		import CrawlSpider, Rule
from scrapy.selector 		import HtmlXPathSelector
from scrapy.linkextractors	import LinkExtractor
from afevent.items			import AfeventItem
from scrapy.http			import Request

 
class MySpider(CrawlSpider):
	name		= "itot"
	allowed_domains	= ["itotelekomforetagen.se"]
	start_urls	= ["https://www.itotelekomforetagen.se/kalendern"]

	rules = (
		Rule(LinkExtractor(allow = (), restrict_xpaths=('//*[@id="search-result"]/tr')), callback="parse", follow = True),
	)
	
 
	def parse(self, response):
		divs = response.xpath('//tbody')
		
		title_list = response.xpath('//*[@id="search-result"]/tr[1]/td[2]/h3/text()').extract()
		# city_list = response.xpath('//*[@class="location"]/a[3]/text()').extract()
		# date_list = response.xpath('//*[@id="conference-listing"]/div/div[2]/ol/li/p[2]/abbr[1]/@title').extract()
		# link_list = response.xpath('//*[@id="conference-listing"]/div/div[2]/ol/li/h4/a/text()').extract()
		# all_list = response.xpath('//*[@id="conference vevent"]/text()').extract()

		# link_list = ['http://lanyrd.com/' + y for y in link_list]
		# for i in range(0, len(city_list)):
		# 	city_list[i].strip

		# print 'link list', len(link_list)
		# #print link_list
		# print 'city list', len(city_list)
		# print city_list
		# print 'date list', len(date_list)
		# print date_list
		print 'title list', len(title_list)
		print title_list
		#print len(all_list)

		# for title, city, date, link in zip(title_list, city_list, date_list, link_list):
		# 	item = AfeventItem()
		# 	item['title'] = title
		# 	item['city'] = city
		# 	item['date'] = date
		# 	request = Request(link_list, callback = self.parse_url)
		# 	requst.meta['item'] = item
		# 	yield request

		yield item

              
		# for x in range(0, len(title_list)):
		# 	item = AfeventItem()
		# 	item['title'] = title_list[x]
		# 	item['city'] = city_list[x]
		# 	item['date'] = date_list[x]
		# 	request = Request(link_list[x], callback = self.parse_url)
		# 	request.meta['item'] = item
		#yield request

 	# def parse_url(self, response):
 	# 	item = response.meta['item']
 	# 	hxs = HtmlXPathSelector(response)
 	# 	link = hxs.select('//*[@class="split first item-meta"]/ul/li/a').extract()
 	# 	item['url'] = hxs.select('/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/span/text()').extract()[0]
 	# 	yield item
