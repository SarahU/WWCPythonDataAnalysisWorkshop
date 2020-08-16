# 3.1 Normalize a 5x5 random matrix
# 3.2 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

import numpy as np
from numpy import array
from numpy.linalg import norm

# 3.1 Normalize a 5x5 random matrix
a = np.random.random(25)
a = a.reshape(5, 5)

scalar_norm = np.linalg.norm(a)

normalised_a = a / scalar_norm
print('original')
print(a)

print('normalised')
print(normalised_a)


# 3.2 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5_x_3 = np.random.random(15)
matrix_5_x_3 = matrix_5_x_3.reshape(5, 3)

matrix_3_x_2 = np.random.random(6)
matrix_3_x_2 = matrix_3_x_2.reshape(3, 2)

matrix_5_x_2 = np.dot(matrix_5_x_3, matrix_3_x_2)

print('real matrix product')
print(matrix_5_x_2)