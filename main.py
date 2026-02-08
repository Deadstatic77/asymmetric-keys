from keyGeneration import KeyGeneration
prime = 251

# << Key generation
A = KeyGeneration.random_matrix(prime)
B = KeyGeneration.random_matrix(prime)

# << Private key components (trapdoor)
Ainv = KeyGeneration.invert_matrix(A, prime)
Binv = KeyGeneration.invert_matrix(B, prime)

# << Public key: expanded quadratic polynomial system
public_key = KeyGeneration.build_public_key(A, B, prime)

# << Example plaintext vector
x = (10, 7, 3)

# << Encrypt using ONLY the public key
cipher = KeyGeneration.encrypt_public(x, public_key, prime)
print("CIPHER:", cipher)

# << Decrypt using private key
plain = KeyGeneration.decrypt(cipher, Ainv, Binv, prime)
print("DECRYPTED:", plain)
