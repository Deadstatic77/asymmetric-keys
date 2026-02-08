import random

class KeyGeneration:
    def __init__(self):
        pass

# << Nonlinear private map (triangular, invertible)
    @staticmethod
    def F_private(x, prime):
        x1, x2, x3 = x
        u1 = (x1 + 2) % prime              # << Simple affine shift
        u2 = (x2 + x1*x1) % prime          # << Quadratic dependency on x1
        u3 = (x3 + x2*x2) % prime          # << Quadratic dependency on x2
        return (u1, u2, u3)

# << Exact inverse of the private nonlinear map
# << Works because of triangular structure
    @staticmethod
    def F_private_inverse(u, prime):
        u1, u2, u3 = u
        x1 = (u1 - 2) % prime
        x2 = (u2 - x1*x1) % prime
        x3 = (u3 - x2*x2) % prime
        return (x1, x2, x3)

# << Multiply a 3x3 matrix by a 3x1 vector mod p
# << Standard linear transformation over finite field
    @staticmethod
    def matrix_vector_multi(M, v, prime):
        return (
            (M[0][0]*v[0] + M[0][1]*v[1] + M[0][2]*v[2]) % prime,
            (M[1][0]*v[0] + M[1][1]*v[1] + M[1][2]*v[2]) % prime,
            (M[2][0]*v[0] + M[2][1]*v[1] + M[2][2]*v[2]) % prime
        )

# << Generate a random invertible 3x3 matrix mod p
# << Determinant check ensures inverse exists
    @staticmethod
    def random_matrix(prime):
        while True:
            M = [[random.randrange(prime) for _ in range(3)] for _ in range(3)]
            determinate = (
                M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1]) -
                M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0]) +
                M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0])
            ) % prime
            if determinate != 0:            # << Invertible matrix condition
                return M

# << Compute inverse of a 3x3 matrix mod p
# << Uses adjugate * modular inverse of determinant
    @staticmethod
    def invert_matrix(M, prime):
        a,b,c = M[0]
        d,e,f = M[1]
        g,h,i = M[2]

        determinate = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)) % prime
        determinate_inverse = pow(determinate, -1, prime)   # << Modular inverse

        # << Adjugate matrix (transpose of cofactor matrix)
        adj = [
            [(e*i - f*h) % prime, (c*h - b*i) % prime, (b*f - c*e) % prime],
            [(f*g - d*i) % prime, (a*i - c*g) % prime, (c*d - a*f) % prime],
            [(d*h - e*g) % prime, (b*g - a*h) % prime, (a*e - b*d) % prime]
        ]

        # << Final inverse matrix
        return [[(determinate_inverse * adj[r][c]) % prime for c in range(3)] for r in range(3)]

# << Gen keypair
    @staticmethod
    def generate_keypair(prime):
        A = KeyGeneration.random_matrix(prime)
        B = KeyGeneration.random_matrix(prime)
    
        Ainv = KeyGeneration.invert_matrix(A, prime)
        Binv = KeyGeneration.invert_matrix(B, prime)
    
        public_key = KeyGeneration.build_public_key(A, B, prime)
        private_key = (Ainv, Binv)
    
        return public_key, private_key

# << Build the PUBLIC KEY
# << Expands AxFxB into explicit quadratic polynomials
# << Each polynomial has 10 coefficients:
# << [x1^2, x2^2, x3^2, x1x2, x1x3, x2x3, x1, x2, x3, 1]
    @staticmethod
    def build_public_key(A, B, prime):
        public_polys = []

        for row in A:                      # << One output polynomial per row of A
            poly = [0]*10

            for k in range(3):             # << Corresponds to F output index
                a = row[k]
                b1, b2, b3 = B[k]

                # << Contribution from F1 = y1 + 2
                if k == 0:
                    poly[6] += a*b1        # << x1 coefficient
                    poly[7] += a*b2        # << x2 coefficient
                    poly[8] += a*b3        # << x3 coefficient
                    poly[9] += 2*a         # << constant term

                # << Contribution from F2 = y2 + y1^2
                if k == 1:
                    poly[0] += a*b1*b1     # << x1^2
                    poly[3] += 2*a*b1*b2   # << x1x2
                    poly[1] += a*b2*b2     # << x2^2
                    poly[6] += a*b2        # << x1
                    poly[7] += a*b3        # << x2

                # << Contribution from F3 = y3 + y2^2
                if k == 2:
                    poly[1] += a*b2*b2     # << x2^2
                    poly[5] += 2*a*b2*b3   # << x2x3
                    poly[2] += a*b3*b3     # << x3^2
                    poly[8] += a*b3        # << x3

            public_polys.append([c % prime for c in poly])

        return public_polys

# << Encrypt using ONLY the public key
# << Evaluates the quadratic polynomials
    @staticmethod
    def encrypt_public(x, public_key, prime):
        x1, x2, x3 = x

        # << Precompute monomials in fixed order
        terms = [
            x1*x1, x2*x2, x3*x3,
            x1*x2, x1*x3, x2*x3,
            x1, x2, x3, 1
        ]

        return tuple(
            sum(c*t for c,t in zip(poly, terms)) % prime
            for poly in public_key
        )

# << Decrypt 
# << Peel off A, then F, then B
    @staticmethod
    def decrypt(cipher, Ainv, Binv, prime):
        y = KeyGeneration.matrix_vector_multi(Ainv, cipher, prime)
        y = KeyGeneration.F_private_inverse(y, prime)
        x = KeyGeneration.matrix_vector_multi(Binv, y, prime)
        return x
