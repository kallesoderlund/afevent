# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf        import settings
from scrapy.exceptions  import DropItem
from pymongo            import MongoClient


class AfeventPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        
    def process_item(self, item, spider):
        if self.collection.find_one({'url': item['url']}):
            raise DropItem('Item already in DB')
        else:
            description = item['description'].lower()
            title = item['title'].lower()
            item['tags'] = []
            keywords = ["fastighet", "commerce", "automatic", "industri", "process", "autmation", "student", "ingenjor", "skog", "digital", "infrastruktur", " it", "samhallsbyggnad", "fisksas"]

            for i in range(len(keywords)):
                if keywords[i] in description or keywords[i] in title:
                    if keywords[i] not in item['tags']:
                        item['tags'].append(keywords[i])
            print item['tags']
            self.collection.insert(dict(item))

        for data in item:
          if not data:
              valid = False
              raise DropItem("Missing {0}!".format(data))
        
        return item

    	

