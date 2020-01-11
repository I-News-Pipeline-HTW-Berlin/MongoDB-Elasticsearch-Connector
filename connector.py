#!/usr/bin/env python3
import elasticsearch
import pymongo
import connector_secrets as sec


es = elasticsearch.Elasticsearch(sec.ELASTICSEARCH_HOST)
mongo = MongoClient(host=sec.MONGO_URI, tz_aware=True)

def extract_mongo_id(document):
    return document[u'_id']

for mongo_id in map(extract_mongo_id, mongo[sec.MONGO_COLLECTION].find(dict(), {"_id":1}))
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
    mongo_doc = mongo[sec.MONGO_COLLECTION].find({"_id":mongo_id})
    mongo_doc[u"mongo_id"] = mongo_doc[u"_id"]
    del mongo_doc[u"_id"]
    es.create(index=sec.ELASTICSEARCH_INDEX,
              body=mongo_doc)