#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:54:17 2019
Author: Wes Bailey
Description:
"""

#Initalize Object#
es = Elasticsearch(HOST="http://localhost", PORT=9200)

doc1 = {"sentence": "Today is a sunny day"}
doc2 = {"sentence": "Today is a bright-sunny day"}
doc3 = {"sentence": "Today is a rainy day."}

es.index(index="english", doc_type = "sentences", id=1, body=doc1)
es.index(index="english", doc_type = "sentences", id=2, body=doc2)
es.index(index="english", doc_type = "sentences", id=3, body=doc3)

#Get Everything#
es.search(index="english", body={"from":0, "size":3,"query":{"regexp":{"sentence":".*"}}})

#Only documents with "sun" as subset#
es.search(index="english", body={"from":0, "size":2,"query":{"regexp":{"sentence":"sun.*"}}})
