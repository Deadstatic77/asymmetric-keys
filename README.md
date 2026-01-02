# DOCUMENTATION <br>
Soon to come

# MATHEMATICAL EXPLANATION <br>
Foreword: This is my understanding of how mathematics works, and my mathematical definitions. I am not sure how correct these are, and I may be completely wrong; but this is how I understand things as they are and how I made this asymmetric system work. I'm not very good at mathematics, so don't come after me for being wrong!

### Modulo <br>
A modulo or mod() is a function that calculates the remainder of a division operation between two numbers. For example, (7/3) = 2 (well actually 2.333...) with a remainder of 1. We can target *only* the remainder with the modulo operator (%). Therefore, (7%3) = 1.

### Matrix <br>
A set of numbers compressed into a table. In python, this can be represented as a 2D list, shown here: <br>
matrix = [[1,2,3],[4,5,6], [6,7,8]]
<br>

### Matrix Determinate <br>
A scalar value that is calculated from the elements of a square matrix, modulo the prime. If the determinate is equal to non zero, then the matrix in invertible. If the determinate is equivalent to zero, then the matrix cannot be inverted.
<br>

### Matrix Determinate Inverse <br>
A determinate inverse is simply just the matrix determinate to the power of negative 1 (-1). 
<br>

### Vector <br>
A three number column. Example: <br>
[x1,x2,x2]
<br>

### Matrix-vector multiplication: <br>
Multiplying the given matrix by the given vector. In this code, the given matrix is a 3x3 square matrix, and the given vector is a 1x3 matrix. Example: <br>
3x3 square matrix ⋅ 1x3 vector matrix is a demonstration of matrix-vector multiplication.
<br>

### Matrix Cross Term <br>
A cross term is a component of an equation that contains a variable that does not belong to that equations intended coordinate. It is produced by a mixing operation such as matrix multiplication. Example: <br>
**random_matrix** = [[1,2,3],[4,5,6], [6,7,8]] <br>
**private_key** = [[x1],[x2],[x3]] = [[9],[10],[11]] <br>
**Matrix-vector multiplication:** y = random_matrix ⋅ private_key <br>
**Compute the first coordinate (of 9):**<br>
**y1** = (1 ⋅ x1) + (2 ⋅ x2) + (3 ⋅ x3) <br>
**y1** = (1 ⋅ 9) + (2 ⋅ 10) + (3 ⋅ 11) <br>
**y1** = (4) + (10) + (18) <br>
**y1** = 32 <br>

1 ⋅ x1 is the **native term** <br>
2 ⋅ x2 is a **cross term** <br>
3 ⋅ x3 is a **cross term** <br>
x2 and x3 (represented as (2 ⋅ 5 = 10) and (3 ⋅ 6 = 18)) are cross terms as they have *crossed* into a coordinate that is meant to represent only x1. This is intentional.

### Matrix Minor <br>
The minor of an element of a matrix is the determinant of the sub-matrix formed by deleting a row and column in which the element is located. Example: <br>
A = [[1,2,3],[4,5,6],[7,8,9]] <br>
The minor of element 1 (position A[0][0]) is the determinant of the 2x2 matrix obtained by removing the first row and first column, which produces: <br>
A[0][0] = [[5,6],[8,9]]
<br>

### Matrix Cofactor (signed minor) <br>
A cofactor of an element of a matrix is equal to the minor of that element multiplied by (-1)^(i+j), where i and j are the rows and column indices of the element.<br>
A cofactor is the signed determinant of the smaller matrix that remains after removing the elements row and column.
<br>

### Matrix Transposition <br>
Matrix transposition is a new matrix that is created by flipping the original matrix over its diagonal, and swapping the rows and columns. For example, <br>
m ⋅ n will transpose into n ⋅ m; turning the element a<sub>ij</sub> into a<sub>ji</sub>
<br>

### Matrix Adjugate <br>
An adjugate matrix is a matrix that is comprised of the cofactors of the original matrix, transposed. The adjugate matrix is necessary when inverting a matrix through the formula <br>
M^(-1)=(1/determinate) ⋅ adjugate(M)<br>
The adjugate matrix does not contain the cross terms within itself; instead when multiplied by the original matrix and scaled by 1/determinant(M), it cancels out all cross terms and produces the original matrix. 
<br>