# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy 	import Item, Field

# The following are the attributes which the spider tries to extract. If an
# attribute is not presented on the website, the attribute will receive a null value. 
class AfeventItem(scrapy.Item):
    title = Field()
    location = Field()
    venue = Field()
    host = Field()
    date = Field()
    link = Field()
    url = Field()
    time = Field()
    description = Field()
    tags = Field()
    type = Field()
