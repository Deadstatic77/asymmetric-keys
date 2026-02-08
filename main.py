from keyGeneration import KeyGeneration
prime = 251

# << Key generation
public_key, private_key = KeyGeneration.generate_keypair(prime)

print("PUBLIC KEY:", public_key)
print("PRIVATE KEY:", private_key)

# << Example plaintext vector
x = (10,7,3)

# << Encryption using only pub key
cipher = KeyGeneration.encrypt_public(x, public_key, prime)
print("CIPHER:", cipher)

# << Encryption using only priv key
plain = KeyGeneration.decrypt(cipher, *private_key, prime)
print("DECRYPTED:", plain)
