from decode import get_list_threat_words
from analitic_threat import calculate_threat_percentage
from mongo_config import get_from_mongo
from elastic_search import update_mapping_for_es

import os
from dotenv import load_dotenv

load_dotenv()

high_level_encoded = os.getenv('ENCODE_LEVEL_HIGH')
low_level_encoded = os.getenv('ENCODE_LEVEL_LOW')


def run_decoding_service():
    update_mapping_for_es()
    for value in get_from_mongo():
        high_lelvel_list = get_list_threat_words(high_level_encoded).split()
        low_level_list = get_list_threat_words(low_level_encoded).split()
        percent_bds = calculate_threat_percentage(high_lelvel_list, low_level_list, value['text'])
