#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:48:47 2019
Author: Wes Bailey
Description:
"""

from elasticsearch import Elasticsearch

#Initalize Object#
es = Elasticsearch(HOST="http://localhost", PORT=9200)

doc1 = {"sentence": "Today is a sunny day"}
doc2 = {"sentence": "Today is a bright-sunny day"}


es.index(index="english", doc_type = "sentences", id=1, body=doc1)
es.index(index="english", doc_type = "sentences", id=2, body=doc2)

res = es.search(index="english", body={ "from": 0, "size": 0, "query": { "bool": { "must_not": { "match": { "sentence": "bright" } }, "should": { "match": { "sentence": "sunny" } } } } })
res

res = es.search(index="english", body={ "from": 0, "size": 1, "query": { "bool": { "must_not": { "match": { "sentence": "bright" } }, "should": { "match": { "sentence": "sunny" } } } } })
res
