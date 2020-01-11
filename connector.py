#!/usr/bin/env python3
import elasticsearch
import pymongo
import connector_secrets as sec


es = elasticsearch.Elasticsearch(sec.ELASTICSEARCH_HOST)
mongo = pymongo.MongoClient(host=sec.MONGO_URI, tz_aware=True)

mongo_coll = mongo[sec.MONGO_DATABASE][sec.MONGO_COLLECTION]

def extract_mongo_id(document):
    return document[u'_id']

for mongo_id in map(extract_mongo_id, mongo_coll.find(dict(), {"_id":1})):
    indexed_object = es.search(index= sec.ELASTICSEARCH_INDEX,
                        size = 1,
                        body= {"query":{
                            "bool":{
                                "must":{
                                    "match":{
                                        "mongo_id":str(mongo_id)
                                    }
                                }
                            }
                        }})
    already_indexed = indexed_object["hits"]["total"]["value"] == 0
    if already_indexed:
        continue
    mongo_doc = mongo_coll.find_one({"_id":mongo_id})
    mongo_doc[u"mongo_id"] = mongo_doc[u"_id"]
    del mongo_doc[u"_id"]
    es.create(index=sec.ELASTICSEARCH_INDEX,
              body=mongo_doc)