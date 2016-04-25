# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json

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
        with open("keywords_final.json") as json_file:
            global json_data
            json_data = json.load(json_file)

        with open("type.json") as json_file:
            global json_data2
            json_data2 = json.load(json_file)
        
    def process_item(self, item, spider):
        if self.collection.find_one({'url': item['url']}):
            raise DropItem('Item already in DB')
        else:
            description = item['description'].lower()
            title = item['title'].lower()
            item['tags'] = []
            item['type'] = []

            for type1_word in json_data2:
                for type2_word in json_data2[type1_word]:
                    if type2_word.lower() in description or type2_word.lower() in title:
                        if type1_word not in item['type']:
                            item['type'].append(type1_word)

            for level1_word in json_data:
                for level2_word in json_data[level1_word]:
                    if level2_word.lower() in description or level2_word.lower() in title:
                        if level1_word not in item['tags']:
                            item['tags'].append(level1_word)


            self.collection.insert(dict(item))

        for data in item:
          if not data:
              valid = False
              raise DropItem("Missing {0}!".format(data))
        item['location'] = item['location'].strip()
        return item

    	

