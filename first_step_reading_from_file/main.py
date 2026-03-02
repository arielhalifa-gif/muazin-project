from pathlib import Path
from data_reader import read_wav_file
from metadata import extract_metadata
from kafka_producer import publish_kafka
import logging


def run():
    directory_path = Path('data')
    for file in directory_path.rglob('*.wav'):
        text_from_audio = read_wav_file(file)
        metadata = extract_metadata(file)
        value_for_topic = {
            "metadata": metadata,
            "text file": text_from_audio
        }
        publish_kafka(value_for_topic)
        logging.Logger("send to kafka successfully")

if __name__ == "__main__":
    run()