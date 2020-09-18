import pymongo
from zenfinder.config import mongo_url

mongo_client = pymongo.MongoClient(mongo_url)
zenfinder_db = mongo_client['zenfinder']

# define all tables
device_table = zenfinder_db['light_devices']