from kafka_consumer import get_from_kafka


def run():
    for value in get_from_kafka():
        metadata = value['metadata']
        stt = value['text_file']