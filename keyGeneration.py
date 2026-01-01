import random

# VARS
prime = 251

class KeyGeneration:
    def __init__(self):
        pass

# Encryption and creation of private key
    def F_private(x):
        x1, x2, x3 = x
        u1=(x1 + 2) % prime
        u2=(x2 + x1*x1) % prime
        u3=(x3 + x2*x2) % prime
        return (u1,u2,u3)

# Decryption of private key
    def F_private_inverse(u):
        u1,u2,u3=u
        x1=(u1 - 2) % prime
        x2=(u2 - x1*x1) % prime
        x3=(u3 - x2*x2) % prime
        return (x1,x2,x3)
    
    def matrix_vector_multi(M,v): # M = 3x3 matrix  || v = vector
        return (
        (M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2]) % prime, # << Multiplying random 3x3 matrix by the vector to mash the numbers together
        (M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2]) % prime, # << Essentially just 3x3 matrix multiplied by 3x1 matrix to equal 1x3 matrix
        (M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2]) % prime  # << But every column is a mash of all 3 variables (x1,x2,x3) aka vectors
        )
    
    def random_matrix(): # << Generate a random 3x3 matrix
        while True:
            M = [[random.randrange(prime) for _ in range(3)] for _ in range(3)]
            det = ( # << det = determinant || Determines if square matrix is invertible
                M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) -
                M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) +
                M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
            ) % prime
            if det != 0: # << If det != 0 then matrix has an inverse order ELIF det = 0 then matrix does not have an inverse
                return M
            
    def Public(x):
        y = KeyGeneration.matrix_vector_multi(KeyGeneration.random_matrix(), x)
        y = KeyGeneration.F_private(y)
        y = KeyGeneration.matrix_vector_multi(KeyGeneration.random_matrix(), y)
        return y
    
    def PrivateDecrypt(cipher):
        y = KeyGeneration.matrix_vector_multi()