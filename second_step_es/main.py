from kafka_consumer import get_from_kafka
from second_step_es.metadata import calculate_hash_uuid


def run():
    for value in get_from_kafka():
        metadata = value['metadata']
        stt = value['text_file']
        hash_id = calculate_hash_uuid(stt)
        