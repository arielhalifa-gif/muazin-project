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



encoded_string = '''R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
        cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
        ixSZWZ1Z2VlcyxJQ0MsQkRT'''

encoded_string2 = '''RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQY
                    Wxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='''

# Convert the Base64 string to bytes
encoded_bytes = encoded_string.encode('ascii')


# Decode the base64 bytes
decoded_bytes = base64.b64decode(encoded_bytes)

# Convert the resulting bytes back to the original string format
decoded_string = decoded_bytes.decode('utf-8')

# print(f"Encoded string: {encoded_string}")
# print(f"Decoded string: {decoded_string}")
