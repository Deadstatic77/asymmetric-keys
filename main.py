from keyGeneration import KeyGeneration
prime = 251

B = KeyGeneration.random_matrix(prime)
A = KeyGeneration.random_matrix(prime)

Binv = KeyGeneration.invert_matrix(B, prime)
Ainv = KeyGeneration.invert_matrix(A, prime)