#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:56:08 2019
Author: Wes Bailey
Description:
"""

from elasticsearch import Elasticsearch

#Initalize Object#
es = Elasticsearch(HOST="http://localhost", PORT=9200)

#Create Index
es.indices.create(index="first_index", ignore=400)

#Check Index
es.indices.exists(index="first_index")

#Delete Index
es.indices.delete(index="first_index")

doc1 = {"city": "New Delhi", "country":"India"}
doc2 = {"city": "London", "country":"England"}
doc3 = {"city": "Los Angeles", "country":"USA"}

es.index(index="cities", doc_type="places", id=1, body=doc1) 
es.index(index="cities", doc_type="places", id=2, body=doc2) 
es.index(index="cities", doc_type="places", id=3, body=doc3) 

res = es.get(index="cities", doc_type="places", id=2)
res['_source']

