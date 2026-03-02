from confluent_kafka import Producer
import json

producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def publish_kafka(metadata: dict):
    value = json.dumps(metadata).encode('utf-8')
    producer.produce(
        topic="from-text",
        value=value
    )