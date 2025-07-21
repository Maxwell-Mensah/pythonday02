import hashlib
import random
import string


def my_password_hash(password):
    salt = ''.join(random.choices(string.ascii_lowercase, k=4))
    passw=salt+password
    pass_hash= hashlib.md5(passw.encode()).hexdigest()
    return {'hash' : pass_hash,
            'salt': salt }

def my_password_verify(password, salt, hash):
    ht=hashlib.md5((salt+password).encode()).hexdigest()
    return hash==ht


result=my_password_hash("toto")
print(my_password_verify("toto", result["salt"], result['hash']) )