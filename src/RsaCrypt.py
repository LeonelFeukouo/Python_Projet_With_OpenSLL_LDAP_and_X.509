import rsa
from OpenSSL import crypto


def generate_keys(userId):
    (pubKey, privKey) = rsa.newkeys(1024)
    with open(f'Certificates/{userId}.pub', "wb") as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open(f'Certificates/{userId}.key', "wb") as f:
        f.write(privKey.save_pkcs1('PEM'))


def load_keys(userId):
    with open(f'Certificates/{userId}.crt', 'r') as f:
        crt = f.read()
    pub_key_obj = crypto.load_certificate(crypto.FILETYPE_PEM, crt).get_pubkey()
    pub_key = crypto.dump_publickey(crypto.FILETYPE_PEM, pub_key_obj)
    pubKey = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)

    with open(f'Certificates/{userId}.key', 'r') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey


def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')


def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

