import base64

def ascii85_decode(encoded_str):
    encoded_bytes = encoded_str.encode('utf-8')
    decoded_bytes = base64.a85decode(encoded_bytes)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str