import scrapy
from scrapy.spiders 			import CrawlSpider, Rule
from scrapy.selector 			import HtmlXPathSelector
from scrapy.linkextractors		import LinkExtractor
from afevent.items				import AfeventItem
from scrapy.http				import Request

#Instantiates spider class, and sets up allowed domain and start page to crawl
class MySpider(CrawlSpider):
	name		= "dfs2"
	allowed_domains	= ["natverk.dfs.se"]
	start_urls	= ["https://natverk.dfs.se/pagang"]

	# Defines the rules upon which the spider will determine which links to follow.
	# It allows all kind of links, but will only look for them according to the 
	# XPaths given.
	rules = (
		Rule(LinkExtractor(allow = (), restrict_xpaths=('//*[@id="content"]/div[1]/div[4]/div/table[2]/tbody/tr[5]/td[3]/div[2]/a')), callback="parse", follow = True),

	)
 	
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
		divs = response.xpath('//tbody/tr')
		for div in divs:

			item = AfeventItem()
			item['location'] = div.xpath('./td[4]/text()').extract_first().strip()
			item['title'] = div.xpath('./td/div[@class = "event-title"]/span[@class = "link"]/text()').extract()[0]
			item['description'] = div.xpath('./td[3]/div[2]/div//text()').extract()[0]
			date_time = div.xpath('./td[1]/span/text()').extract()[0].split(' ')
			item['date'] = date_time[0]
			item['time'] = date_time[1]
			item['host'] = div.xpath('./td[5]/a/text()').extract()[0]
			url = div.xpath('./td[3]/div[2]/a/@href').extract()[0]
			url = 'https://natverk.dfs.se' + url
			item['url'] = url
			request = Request(url, callback = self.parse_url)
			request.meta['item'] = item
			yield request

	# This def recieves a request and all attributes scraped by "parse".
	# It then looks for the url to the event at a given place and passes all
	# scraped attributes to the database.
 	def parse_url(self, response):
 		item = response.meta['item']
 		#print response.url
 		#skriv = response.xpath('//*[@id="content"]/div[1]/h1/text()').extract()
 		#print skriv
 		#item['description'] = ''.join(response.xpath('//*[@id="content"]/div[1]/article/div[5]/div/div/text()').extract()).strip()
 		yield item