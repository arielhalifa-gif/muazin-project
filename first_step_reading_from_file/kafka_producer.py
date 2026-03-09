from confluent_kafka import Producer
import json
import logger as l

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def publish_kafka(metadata: dict):
    l.logger.info('sending to kafka....')
    value = json.dumps(metadata).encode('utf-8')
    producer.produce(
        topic="from-text",
        value=value
    )
    producer.flush()