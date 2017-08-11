import os
import time
import subprocess
from pymongo import MongoClient

mongoUrl = os.environ.get('MONGOURL', "mongodb://mongodb:27017")
elasticsearchUrl = os.environ.get('ELASTICSEARCHURL',"elasticsearch:9200")

client = MongoClient(mongoUrl)

print("Mongodb server at", mongoUrl)

while True:
    if client.database.command('isMaster')['ismaster']:
        print("Mongod node is now primary")
        break
    else:
        print("Waiting for Mongod node to assume primary status...")
        time.sleep(3)

time.sleep(1)

subprocess.call([
    'mongo-connector',
    '-c',
    '/data/config.json',
    '-m',
    mongoUrl,
    '-t',
    elasticsearchUrl,
    '-d',
    'elastic2_doc_manager',
    '--stdout'
])
