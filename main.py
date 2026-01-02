from keyGeneration import KeyGeneration
prime = 251

# << Gen random invertible matrix
B = KeyGeneration.random_matrix(prime)
A = KeyGeneration.random_matrix(prime)

# << Compute inverse
Binv = KeyGeneration.invert_matrix(B, prime)
Ainv = KeyGeneration.invert_matrix(A, prime)

# << Original private key
x = (10,7,3)

# << Encrypt
cipher = KeyGeneration.Public(x,B,A,prime)
print("CIPHER: ", cipher)

# << Decrypt
decrypt = KeyGeneration.PrivateDecrypt(cipher, Ainv, Binv, prime)
print("DECRYPTED: ", decrypt)