import random

class KeyGeneration:
    def __init__(self):
        pass

# Encryption and creation of private key
    def F_private(x, prime):
        x1, x2, x3 = x
        u1=(x1 + 2) % prime
        u2=(x2 + x1*x1) % prime
        u3=(x3 + x2*x2) % prime
        return (u1,u2,u3)

# Decryption of private key
    def F_private_inverse(u, prime):
        u1,u2,u3=u
        x1=(u1 - 2) % prime
        x2=(u2 - x1*x1) % prime
        x3=(u3 - x2*x2) % prime
        return (x1,x2,x3)
    
    def matrix_vector_multi(M,v, prime): # M = 3x3 matrix  || v = vector
#! A matrix in python can be represented as a 2D list in the form of:  matrix = [[1,2,3],[4,5,6],[7,8,9]] for a 3x3 matrix
        return (
        (M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2]) % prime, # << Multiplying random 3x3 matrix by the vector to mash the numbers together
        (M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2]) % prime, # << Essentially just 3x3 matrix multiplied by 3x1 matrix to equal 1x3 matrix
        (M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2]) % prime  # << But every column is a mash of all 3 variables (x1,x2,x3) aka vectors
        )
    
    def random_matrix(prime): # << Generate a random 3x3 matrix
        while True:
            M = [[random.randrange(prime) for _ in range(3)] for _ in range(3)]
            determinate = ( # << det = determinant || Determines if square matrix is invertible
                M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) -
                M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) +
                M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
            ) % prime    # << A determinate is a scalar value that is calculated from the elements of a square matrix
            if determinate != 0: # << If det != 0 then matrix has an inverse order ELIF det = 0 then matrix does not have an inverse
                return M
            
    def modulo_inverse(x,p):
        return pow(x,-1,p)

    def invert_matrix(M,p):
        a,b,c = M[0]
        d,e,f = M[1]
        g,h,i = M[2]

        # << 
        determinate = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)) % p
        determinate_inverse = KeyGeneration.modulo_inverse(determinate, p)

        # << ADJUGATE MATRIX (Cofactor transpose)
        adj = [
        [(e*i - f*h) % p, (c*h - b*i) % p, (b*f - c*e) % p],
        [(f*g - d*i) % p, (a*i - c*g) % p, (c*d - a*f) % p],
        [(d*h - e*g) % p, (b*g - a*h) % p, (a*e - b*d) % p]
    ]
        
        M_inv = [[(determinate_inverse * adj[r][c]) % p for c in range(3)] for r in range(3)]
        return M_inv


    def Public(x, B, A, prime):
        y = KeyGeneration.matrix_vector_multi(B,x,prime)
        y = KeyGeneration.F_private(y, prime)
        y = KeyGeneration.matrix_vector_multi(A, y, prime)
        return y
    
    def PrivateDecrypt(cipher, Ainv, Binv, prime):
        y = KeyGeneration.matrix_vector_multi(Ainv, cipher, prime)
        y = KeyGeneration.F_private_inverse(y, prime)
        x = KeyGeneration.matrix_vector_multi(Binv, y, prime)
        return x