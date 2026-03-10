from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

es = Elasticsearch('http://localhost:9200')
def create_index():
    mapping = {"mapping": {
        "properties": {
                "size": {"type": int},
                "file_name": {'type': str},
                "creation_date": {'type': datetime},
                "last_modified_date": {'type': datetime},
        }
    }}

    response = es.indices.create(index='muazin', body=mapping)
    logger.info('index created')

# def insert_bulk(actions):
#     bulk(es, actions)
#     logger.info('bulk inserted succesffully')

def send_metadata_to_es(metadata: dict, hash):
    es.index(index='muazin', id=hash, document=metadata)