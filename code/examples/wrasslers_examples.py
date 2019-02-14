
import csv
import os
from elasticsearch import Elasticsearch

#Initalize Object#
es = Elasticsearch(HOST="http://localhost", PORT=9200)

#Create an index in ES, ignore status code 400 (index already exists)
es.indices.create(index = "wrasslers",ignore=400)

#Build the csv indices using your csv data#
with open(os.path.expanduser("~/Projects/Elastic-Search/data/wwf.csv")) as f:
    reader = csv.DictReader(f)
    for line in reader:
        #If uniaue ID in excel file ne _source unique ID
        es.index(index="wrasslers", doc_type = "world_champions", body = line)

 

#Match Query#
#http://localhost:9200/wrasslers/_search?q=cena
es.search(index="wrasslers", body={
    "query": {
        "multi_match" : {
            "query" : "kane",
            "fields" : ["Date", "Days", "Description", "ID", "Location", "Reign", "Show", "Wrestler^3"]
            }
        }
    }
)

#Boost Ressults using certain field#
es.search(index="wrasslers", body={
    "query": {
        "multi_match" : {
            "query" : "cena",
            "fields" : ["Date", "Days", "Description", "ID", "Location", "Reign", "Show", "Wrestler^3"]
            }
        }
    }
)
    
es.search(index="wrasslers", body={
    "query": {
        "multi_match" : {
            "query" : "wes bailey",
            "fields" : ["Date", "Days", "Description^5", "ID", "Location", "Reign", "Show", "Wrestler"]
            }
        }
    }
)
