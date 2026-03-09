import base64

# data = '''R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
#         cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
#         ixSZWZ1Z2VlcyxJQ0MsQkRT'''


# # Encode the string to bytes, then base64 encode the bytes
# encoded_bytes = base64.b64encode(data.encode('utf-8'))

# # To get a string representation of the Base64 data, decode the result as ASCII
# encoded_string = encoded_bytes.decode('ascii')

# print(f"Original string: {data}")
# print(f"Encoded bytes: {encoded_bytes}")
# print(f"Encoded string: {encoded_string}")

def get_list_threat_words(b64_encoded: str):
    encoded_bytes = b64_encoded.encode('ascii')
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string



encoded_string_threat = '''R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
        cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
        ixSZWZ1Z2VlcyxJQ0MsQkRT'''

encoded_string2 = '''RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQY
                    Wxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='''

# Convert the Base64 string to bytes
encoded_bytes_threat = encoded_string_threat.encode('ascii')
encoded_bytes2 = encoded_string2.encode('ascii')


# Decode the base64 bytes
decoded_bytes_threat = base64.b64decode(encoded_bytes_threat)
decoded_bytes2 = base64.b64decode(encoded_bytes2)

# Convert the resulting bytes back to the original string format
decoded_string_threat = decoded_bytes_threat.decode('utf-8')
decoded_string2 = decoded_bytes2.decode('utf-8')

# print(f"Encoded string: {encoded_string_threat}")
# print(f"Decoded string: {decoded_string_threat}")
# print(f"Encoded string2: {encoded_string2}")
# print(f"Decoded string2: {decoded_string2}")