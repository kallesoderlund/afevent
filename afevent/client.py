import pymongo
import json

from scrapy.conf        import settings
from scrapy.exceptions  import DropItem
from pymongo            import MongoClient

client = MongoClient(host=MONGO_HOST,port=27017,max_pool_size=200)
client.drop_database("eventDB")