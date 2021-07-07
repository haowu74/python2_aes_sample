from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import base64

def main():

    #key = '0724955629056261'
    key = '0000000000000000'
    # encrypted_data = 'THClT/T/QRjxTNjhhN7F6SiV0lUehwuIKb4xs1re64M/Sw6WPu4+A08Wx7pNR05lTy4/+k8Q2nnPJdy1B32vEQvtsSfjCz2R1egw/hzc7h+T7DL6jEMWD/ikgCxUjS/Vi252CEECe/zYNlK7zzdpJ/TUPMlQehHg0X JNmN8RUWEMbbOx5UPYaqIJyp8Id/Uq'
    # encrypted_data = 'GiEOmbdSYJRtZPC2yl94gcEWE/Okw9lGoE4mUTtZSYA+l58RGqsBmhG9KOPA8TfDukmwpDFPZm+OXISsz3ttCHencSCe7noLAyaLOK+VEI+W9u+22MwHGqxZDGpI7XfD1rFV2plOxEuc9aXzL+oqrIrw9prgn8LkqmKYU1/laZJqhS/kCtfxL0MgDHewh34vV/ri37rfBcJ4u2yE2+0Eqg=='
    encrypted_data = 'tlUB5OD7dxIXqkNFA4A4YlGv+5+9gomJXVmQrBOF81iwG5VWOqRdwE4Y66cvDNiDeZOa5rSadN8527sJjU3bi/QX/+ERDuxM6FHbJtoF8PxdD8roKHlwiISMiwaoNvuxiRhgE2XS8X7xBylJtlLogxYo/6+wR8k2fX4ruzygadi8qzLxPOM6s23AgRCysAhfq7vseZhu+sQcGomQajCzVQ=='
    
    iv = key[::-1]
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    res = base64.standard_b64decode(encrypted_data.encode("utf8"))
    msg = aes.decrypt(res).decode("utf8")
    original_data = msg[0:-ord(msg[-1])]
    print original_data 

if __name__ == '__main__':
    main()