from kafka_consumer import get_from_kafka
from second_step_es.metadata import calculate_hash_uuid
from mongo_config import send_to_mongo


def run():
    actions = []
    for value in get_from_kafka():
        metadata = value['metadata']
        stt = value['text_file']
        hash_id = calculate_hash_uuid(stt)
        #sending the stt file to mongo
        send_to_mongo(stt)
        action = {
            '_index': 'muazin',
            '_id': hash_id,
            '_source': metadata
        }        