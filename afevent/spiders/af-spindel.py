import scrapy
from scrapy.spiders         import CrawlSpider, Rule
from scrapy.selector        import HtmlXPathSelector
from scrapy.linkextractors  import LinkExtractor
from afevent.items          import AfeventItem
from scrapy.http            import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class myItems(scrapy.Item):
  title       = scrapy.Field()
  city        = scrapy.Field()
  venue       = scrapy.Field()
  date        = scrapy.Field()
  time        = scrapy.Field()
  description = scrapy.Field()
  host        = scrapy.Field()
  url         = scrapy.Field()

class MySpider(CrawlSpider):
  name            = "af"
  allowed_domains = ["afconsult.com"]
  start_urls      = ["http://www.afconsult.com/sv/jobba-hos-oss/event-seminarier--massor/"]
  rules           = (Rule(SgmlLinkExtractor(allow = (), restrict_xpaths=('//*[@id="CalendarContainer"]/div/div/a')), callback="parser", follow = True),
                    )

  def parser(self, response):
    divs = response.xpath('//body')
    item = myItems()
    title_list = divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/h1/text()').extract()
    date_list = divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/span/text()').extract()
    url_list = divs.xpath('//*[@id="mainContent"]/main/section[3]/div[1]/div[1]/article/p[5]/a/@href').extract()

    item['title'] = title_list
    item['date'] = date_list
    item['url'] = url_list

    yield item












                          
                                                    

                                                    



