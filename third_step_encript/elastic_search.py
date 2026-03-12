from elasticsearch import Elasticsearch
from logger_step_three import logger

es = Elasticsearch('http://localhost:9200')

def update_mapping_for_es():
    new_field_mapp = {
        'properties': {
            'percent_bds': {'type': float}
        }
    }
    es.indices.put_mapping(index='muazin', body=new_field_mapp)
    logger.info('mapped new index')


def insert_percent_to_es(with_percent_bds, hash_id):
    es.index(index='muazin', id=hash_id, document=with_percent_bds)
    logger.info('inserted to elastic')


def build_new_document():
    pass