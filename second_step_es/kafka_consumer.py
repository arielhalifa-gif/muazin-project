from confluent_kafka import Consumer
import json



consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "muazin",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["from-text"])

def get_from_kafka():
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue

            value = msg.value().decode("utf-8")
            order = json.loads(value)
    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")

    finally:
      consumer.close()

    return order