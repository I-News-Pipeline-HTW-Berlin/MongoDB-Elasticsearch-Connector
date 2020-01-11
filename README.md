# MongoDB-Ealsticsearch Connector

This Connector copies all files from a MongoDB collection to an Elastisearch index
When re-run, the already copied Documents will not be added again.
The ObjectID from the MongoDB will determine, whether a document was already tranfered.
In the ElasticSearch index, the string of the ObjectID of the MongoDB will be used as the document id.

for it to run, the following packages are required:
  elasticsearch
  pymongo

you can install them via
  sudo pip install pymongo
  sudo pip install elasticsearch

To specify the MongoDB location and collection, as well as the Elasticsearch host and index, create a connector_secrets.py with the following variables:
- MONGO_URI with an URI as specified by https://docs.mongodb.com/manual/reference/connection-string/
- MONGO_DATABASE with the name of the specified Database
- MONGO_COLLECTION with the name of the collection to be indexed
- ELASTICSEARCH_HOST with the URI to the host of Elastisearch
- ELASTICSEARCH_INDEX with the index-name for the MongoDB data
