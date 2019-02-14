#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:24:03 2019
Author: Wes Bailey
Description:
"""

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

#Documents
doc1 = {"city": "New Delhi", "country":"India", "datetime":"2018,01,01,10,20,00"}
doc2 = {"city": "London", "country":"England", "datetime":"2018,01,02,03,12,00"}
doc3 = {"city": "Los Angeles", "country":"USA", "datetime":"2018,04,19,21,02,00"}

#Create indices#
es.index(index="travel", doc_type="cities", id=1, body=doc1) 
es.index(index="travel", doc_type="cities", id=2, body=doc2) 
es.index(index="travel", doc_type="cities", id=3, body=doc3) 

#Use get mapping to figure out the mapping ES has created#
#Check result to see datetime wasn't mapped as a datetime element#
#When this occurs, you need to adjust ES' default mapping#
es.indices.get_mapping(index="travel", doc_type="cities")

#MUST DELETE INDEX
es.indices.delete(index="travel")

#Recreate#
es.indices.create(index="travel")

#Change Mapping to adjust for datetime#
#TIP: Copy what was provided automatically and make adjustments#
es.indices.put_mapping(
    index="travel",
    doc_type="cities",
    body=
        {

                "properties": {
                    "city": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "country": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "datetime": {
                        "type": "date",
                        "format":"yyyy,MM,dd,hh,mm,ss"
                    }
                }
            }
)

#Check mapping results with adjustment#
es.indices.get_mapping(index="travel", doc_type="cities")
