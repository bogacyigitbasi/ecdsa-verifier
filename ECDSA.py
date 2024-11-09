from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError

import hashlib

def sign(message_hash, sign_key_hex):
    #load key

    privKey = SigningKey.from_string(bytes.fromhex(sign_key_hex), curve = SECP256k1)

    return privKey.sign(message_hash)



def verify(message_hash, signature, verifyKey_hex):
    # load pubkey from string
    pubKey = VerifyingKey.from_string(bytes.fromhex(verifyKey_hex), curve=SECP256k1)

    try:
        #verify
        pubKey.verify(signature, message_hash)
        print("Signature is verified")
    except BadSignatureError:
        print("Signature verification failed")

#generate the key pair using secp256k1
key_generate = SigningKey.generate(curve=SECP256k1)
# private key
signKey_hex = key_generate.to_string().hex()
# public key
verifyKey_hex = key_generate.verifying_key.to_string().hex()


# message to sign
message = "ECDSA message to sign"
# sha256 of the message for best practice and manageable size.
message_hash = hashlib.sha256(message.encode())
message_hash_hex = message_hash.digest()

print("SHA256:", message_hash_hex.hex())
signature = sign(message_hash_hex, signKey_hex)
print("Signature = (r,v)", signature)

verify(message_hash_hex, signature, verifyKey_hex)