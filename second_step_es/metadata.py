import hashlib

def calculate_hash_uuid(data_to_convert):
    data_encoded = data_to_convert.encode('etf-8')
    hash_object = hashlib.sha256(data_encoded)
    hex_data = hash_object.hexdigest()
    return hex_data