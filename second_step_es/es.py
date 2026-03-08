from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch('http://localhost:9200')

mapping = {"mapping": {
    "properties": {
            "size": {"type": int},
            "file_name": {'type': str},
            "creation_date": {'type': datetime},
            "last_modified_date": {'type': datetime},
            "stt": {'type': object}
    }
}}

response = es.indices.create(index='second step', body=mapping)