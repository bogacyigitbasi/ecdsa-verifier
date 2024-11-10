from ecdsa import SigningKey, VerifyingKey, SECP256k1, BadSignatureError

import hashlib

def sign(message_hash, sign_key_hex):
    #load key

    privKey = SigningKey.from_string(bytes.fromhex(sign_key_hex), curve = SECP256k1)

    return privKey.sign(message_hash)


def verify_with_pubkey(message_hash, signature, verifyKey_hex):
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

# to decode the signature
from ecdsa.util import sigdecode_string

(r,s ) = sigdecode_string(signature, SECP256k1.order)
print("Signature = (r,s)", signature.hex())

verify_with_pubkey(message_hash_hex, signature, verifyKey_hex)

#####

# curve is y^2 = x^3 + 7
def calculate_R_points(x):
    y_squared = (x**3 + 7) % SECP256k1.curve.p
    y = pow(y_squared, (SECP256k1.curve.p+1)//4, SECP256k1.curve.p)
    return y, SECP256k1.curve.p - y



def recover_public_key(message_hash, r,s,):
    # Public Key =s-¹⋅(messageHash⋅G+r⋅R) mod n

    R = calculate_R_points(r)
    print(R)
    for Ri in R:
        tempPubKey = pow(s, -1, SECP256k1.order)*(message_hash*SECP256k1.generator+Ri)
        if verify_with_pubkey(message_hash,signature, tempPubKey):
            return tempPubKey


