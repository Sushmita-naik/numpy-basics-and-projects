
# matrix in numpy
import numpy as np
matrix=np.matrix([
    [1,2,3,4,5],
    [6,7,8,8,9]
])
matrix2=np.matrix([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print(matrix)
print(matrix2.T)
print(matrix.dot(matrix2.T))

import numpy as np
matrix=np.matrix([1,2,3,4,5,6])
print(matrix)
print(matrix*matrix.T)
matrix2=np.matrix([[1,2],[3,4]])
print(matrix2*matrix2)
