import base64

def e85(input_str):
    input_bytes = input_str.encode('utf-8')
    encoded_bytes = base64.a85encode(input_bytes)
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str
