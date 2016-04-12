import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors.sgml	import SgmlLinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request
from urlparse 					import urljoin

#Instantiates spider class, and sets up allowed domain and start page to crawl
class MySpider(CrawlSpider):
	name		= "lanyrd"
	allowed_domains	= ["lanyrd.com"]
	start_urls	= ["http://lanyrd.com/places/sweden/"]

	# Defines the rules upon which the spider will determine which links to follow.
	# It allows all kind of links, but will only look for them according to the 
	# XPaths given.
	rules = (
		Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="conference-listing"]/div/div[2]/ol/li/h4/a')), callback="parse", follow = True),
	)


	def parse(self, response):
		i = 0
		#url_list = []

 	
 	# This def starts with setting an index to 0. The for loop will extract all the 
 	# divs in which the events are located, and then iterate through them one by one. 
 	# AfeventItem() is called to determine which attribute to assign values to.
 	# In every div the spider will look in certain locations for attributes, and
 	# return blank if not found. 
 	# Since not the url to the event isn't present on the start site, the spider will have
 	# to follow the links set up by "rules" to find them. This def thus creates
 	# a request to that link and passes all the attributes to the def 'parse_url'.
 	# It returns this request and then iterates to the next event div. It will
 	# continue to iterate until the index is equal to the amount of event divs.
	def parse(self, response):
		i = 0


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

			url = div.xpath('//h4/a/@href').extract()[i]
			url = 'http://lanyrd.com' + url
			request = Request(url, callback = self.parse_url)

			request.meta['item'] = item

			if i < len(response.xpath('//li[@class="conference vevent"]')):
				i = i + 1	
			yield request


 	def parse_url(self, response):
 		item = response.meta['item']
 		
 		link = response.xpath('//*[@class="split first item-meta"]/ul/li/a').extract()
 		item['url'] = response.xpath('/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/@href').extract()[0]
 		yield item



	# This def recieves a request and all attributes scraped by "parse".
	# It then looks for the url to the event at a given place and passes all
	# scraped attributes to the database.
 	def parse_url(self, response):
 		item = response.meta['item']
 		link = response.xpath('//*[@class="split first item-meta"]/ul/li/a').extract()
 		item['url'] = response.xpath('/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/ul/li[1]/a/@href').extract()[0]
 		yield item

