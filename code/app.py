#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:39:38 2019
Author: Wes Bailey
Description:
"""

from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__, template_folder='/Users/wbailey7/Projects/Elastic-Search/code/templates')
es = Elasticsearch(HOST="http://localhost", PORT=9200)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['Get', 'Post'])
def search_request():
    search_term = request.form["input"]
    res = es.search(
            index="wrasslers",
            size=10,
            body={
                "query": {
                    "multi_match": {
                            "query": search_term,
                            "fields": [
                                "Date",
                                "Days",
                                "Description",
                                "ID",
                                "Location",
                                "Reign",
                                "Show",
                                "Wrestler^3"
                        ]
                    }
                }
            }
    )
    return render_template('results.html', res=res)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)