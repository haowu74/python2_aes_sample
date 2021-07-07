from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import base64
import json

def main():
    key = '0000000000000000'
    original_data = '{"PackageId":"bb022743-1fb9-48d0-800ebac1e3154664","StatusCode":100,"StatusMessage":"Success","DateSent":637260194896070000,"DateReceived":637260194896070000}'

    iv = key[::-1]
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    count = len(original_data.encode('utf-8'))
    add = AES.block_size - (count % AES.block_size)
    entext = original_data + (chr(add) * add)
    res = aes.encrypt(entext.encode("utf8"))
    # msg = str(base64.standard_b64encode(res))
    msg = unicode(str(base64.standard_b64encode(res)), "utf-8")
    print msg 

if __name__ == '__main__':
    main()