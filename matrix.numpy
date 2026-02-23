
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

# function in matrix
# 1.Tranpose of matrix
import numpy as np
array=np.array([1,2,3,4,5,6,7])
print(np.transpose(array))
array2=np.array([
    [1,2,3,4,5,6],
    [6,7,8,9,10,11]
])
print()
print(np.transpose(array2))

# 2.Swapaxes same as transpose
import numpy as np
array=np.array([
    [1,2],
    [3,4],[5,6]
])
print(array)
print(np.swapaxes(array,(0,1)))

# 3.Inverse only for square matrix
import numpy as np
array=np.array([
    [1,2,3],
    [3,4,6],
    [5,6,7]
])
print(array)
print(np.linalg.inv(array))


# 4.Power
import numpy as np
array=np.array([
    [1,2,3],
    [3,4,5],
    [11,12,13]
])
print(array)
power_identity_matrix=np.linalg.matrix_power(array,0)
print(power_identity_matrix)
power_matrix=np.linalg.matrix_power(array,1)
print(power_matrix)
power_matrix2=np.linalg.matrix_power(array,-1)
print(power_matrix2)

# determinate of matrix
import numpy as np
array=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [11,12,13,14],
    [34,54,65,76]
])
determinate_matrix=np.linalg.det(array)
print(determinate_matrix)

