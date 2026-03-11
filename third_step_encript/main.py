from decode import get_list_threat_words
import os
from dotenv import load_dotenv

load_dotenv()

high_level_encoded = os.getenv('ENCODE_LEVEL_HIGH')
low_level_encoded = os.getenv('ENCODE_LEVEL_LOW')


def run_decoding_service():
    high_lelvel_list = get_list_threat_words(high_level_encoded).split()
    low_level_list = get_list_threat_words(low_level_encoded).split()