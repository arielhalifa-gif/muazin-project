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


def update_new_field_es(with_percent_bds, hash_id):
    response = es.update(index='muazin', id=hash_id, body={'doc': {'percent_bds': with_percent_bds}})
    logger.info('inserted to elastic')
    return response['result']