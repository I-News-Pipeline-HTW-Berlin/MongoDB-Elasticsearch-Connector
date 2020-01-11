# MongoDB-Ealsticsearch Connector

This Connector copies all files from a MongoDB collection to an Elastisearch index
When re-run, the already copied Documents will not be added again.
The ObjectID from the MongoDB will determine, whether a document was already tranfered.
In the ElasticSearch index, the ObjectID of the MongoDB will not be named "_id" like in the MongoDB, but "mongo_id"

To specify the MongoDB location and collection, as well as the Elasticsearch host and index, create a connector_secrets.py with the following variables:
- MONGO_URI with an URI as specified by https://docs.mongodb.com/manual/reference/connection-string/
- MONGO_COLLECTION with the name of the collection to be indexed
- ELASTICSEARCH_HOST with the URI to the host of Elastisearch
- ELASTICSEARCH_INDEX with the index-name for the MongoDB data
