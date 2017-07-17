from elasticsearch import Elasticsearch
from pymongo import MongoClient

TIMEOUT = 60
db, collection = ('native_ads', 'ads')
es = Elasticsearch(timeout=TIMEOUT)
es.indices.delete(index=db, ignore=[400, 404])

def index_mongo(db, collection):
	conn = MongoClient()
	coll = conn[db][collection]
	cursor = coll.find({}, {'_id':0})
	print("Indexing in bulk {} documents".format(cursor.count()))

	bulk = []

	for n, item in enumerate(cursor):
		bulk.append({'index':{
			'_index':db,
			'_type':collection,
			'_id':int(n)}})
		bulk.append(item)

	
	es.bulk(index=db, body=bulk, refresh=True)

if __name__ == '__main__':
	 
	index_mongo(db, collection)