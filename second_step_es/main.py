from kafka_consumer import get_from_kafka
from second_step_es.metadata import calculate_hash_uuid
from mongo_config import send_to_mongo
from es import send_metadata_to_es, create_index


def run_elastic():
    # actions = []
    create_index()
    for value in get_from_kafka():
        metadata = value['metadata']
        stt = value['text_file']
        hash_id = calculate_hash_uuid(stt)
        #sending the stt file to mongo
        send_to_mongo(stt)
        send_metadata_to_es(metadata,hash_id)

if __name__ == "__main__":
    run_elastic()