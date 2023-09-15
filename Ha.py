import hashlib

def Hash(Obj):
    a = hashlib.sha512(Obj.encode())
    return a.hexdigest()
