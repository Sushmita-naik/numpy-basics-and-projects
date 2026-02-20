# creating 1d array 
import numpy as np
array=np.array([1,2,3,4,5,6,7])
print(array)
print(array*2)
print(array/3)
print(array+5)
print(array-5)
print(array%3)

# creating 2d arrays
import numpy as np
arraya2d=np.array([
    [12,13,14,15,16],
    [23,45,67,89,67],
    [45,67,89,90,32]
])
print(arraya2d.shape)
print(arraya2d.ndim)
print(arraya2d*8)
print(arraya2d/8)
print(arraya2d+45)
print(arraya2d%6)
print(arraya2d-2)

#creaing 3d arrays
import numpy as np
array3d=np.array([
    [
        [1,2,3,4,5,6],
        [2,3,4,5,6,7],
        [5,6,7,8,9,7]
    ],
    [
        [1,2,3,4,5,6],
        [2,3,4,5,6,7]
    ],
    [
        [4,5,6,7,8,9],
        [7,8,9,90,12,45],
        [4,55,66,77,89,12]
    ]
])
print(array3d*12)
print(array3d.shape)
print(array3d.ndim)

#functions of numpy
# array filled with 0's
import numpy as np
a=np.zeros(10) # for 1d
print(a)
print()
b=np.zeros((2,4))
print(b) #for 2d

# array filled with 1's
import numpy as np
a=np.ones(5) #for 1d
print(a)
b=np.ones((4,6))# for 2d
print(b)


#empty arrays
import numpy as np
a=np.empty(1)
print(a)

# range elements
import numpy as np
a=np.arange(0,10) #without steps
print(a)
b=np.arange(1,12,3) #with steps
print(b)

for diagonol elements
import numpy as np
a=np.eye(4)
print(a)


# linearly spaces values
import numpy as np
a=np.linspace(1,20,7)
print(a)
b=np.linspace(1,100,50)
print(b)

import numpy as np
lab_monitor_sensor=np.zeros((7,24))
hours=np.arange(24)
temp_values=np.linspace(20,40,24)
lab_monitor_sensor[:]=temp_values
maintanance=np.eye(7)
lab_monitor_sensor=lab_monitor_sensor+1
print("Temparature Matrix:\n",lab_monitor_sensor)
print("Maintanance Matrix:\n",maintanance)

# Datatypes
import numpy as np
array1=np.array([1,2,3,4,5,6])
print(array1.dtype)
print(array1)
new_array=array1.astype(float)
print(new_array)
arr=np.array([12,34,56,78])
print(arr.dtype)
print(arr)
arr2=arr.astype(np.float32)
print(arr2.dtype)
print(arr2)

import numpy as np
arr=np.array(["100","200","300"])
print(arr.dtype)
new_array=arr.astype(float)
print(new_array)
print(new_array.dtype)
print(new_array+50)
print(new_array)
new_array2=arr.astype(int)
print(new_array2)
print(new_array2.dtype)


# arithmatic operations in numpy
import numpy as np
array=np.array([1,2,3,4,5,6,7])
print(array+7)
print(array*5)
print(array-9)
print(array/4)

# for 1d
import numpy as np
array=np.array([1,2,3,4,5])
print(array*array)
 
# for 2d
array=np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,15]
])
print(array+5)
print(array*array)
print(array-5)


# shapes in numpy
import numpy as np
array= np.array([1,2,3,4])
print(array.shape)
array2=array.reshape(2,2)
print(array2)
print(array2.shape)
print(array2.ndim)
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.reshape(-1))

# shapes in numpy
import numpy as np
array= np.array([1,2,3,4])
print(array.shape)
array2=array.reshape(2,2)
print(array2)
print(array2.shape)
print(array2.ndim)
arr=np.array([1,2,3,4],ndmin=5)
print(arr)


# broadcasting in numpy
import numpy as np
x=np.array([[1,2,3],[1,2,3],[2,4,6]])
print(x)
y=np.array([[1],[2],[3]])
print(y)
print(x+y)



# indexing in numpy
# for 1d array
import numpy as np
var=np.array([1,2,3,4,5])
print(var[1])
print(var[-1])

#for 2d array
import numpy as np
var2=np.array([[1,2,3,5],[5,6,7,9]])
print(var2)
print(var2.ndim)
print(var2[0,3])

# # for 3d array
import numpy as np
var3=np.array([
    [
        [1,2,3,4,5]
    ],
    [
       [4,5,6,7,8], 
    ],
    [
        [12,4,5,6,7]
    ]
])
                
                
print(var3.ndim)
print(var3)
print(var3[1,0,2])
print(var3.shape)

# slicing for 1d
import numpy as np
x=np.array([1,2,3,4])
print(type(x))
print(x.shape)
print(x.ndim)
print(x[0:]) 
print(x[-4:-1])
print(x[0:5:2])

# for 2d array
import numpy as np
y=np.array([
    [1,2,3,4,5],
    [2,3,4,5,6],
    [6,7,8,9,10]
])
print(y.ndim)
print(y.shape)
print(y[1,2:])
print(y[0,0:5:2])
print(y[2,1:6:2])

# for 3d array
import numpy as np
A = np.arange(1,25).reshape(2,3,4)

print("Full 3D Array:\n", A)
print("Shape:", A.shape)   


print("\nFirst layer:")
print(A[0])

print("\nSecond layer, second row:")
print(A[1,1])

print("\nSingle element:")
print(A[1,1,2])

print("\nAll layers, first row:")
print(A[:,0,:])

print("\nFirst layer, first two rows:")
print(A[0,0:2,:])

print("\nAll layers, last two columns:")
print(A[:,:,-2:])

print("\nEvery second column:")
print(A[:,:,::2])

print("\nSecond layer, all rows, last column:")
print(A[1,:, -1])

# iteration statements in numpy array
# for 1d array
import numpy as np
x=np.array([1,2,3,4,5,6,7])
print(x)
print()
for i in x:
    print(i)

# for 2d array
import numpy as np
array=np.array([
    [1,2,3,4,5,6],
    [3,4,5,6,7,8]
)]
print(array)
for i in array:
    for j in i:
        print(j)


# for 3d array
import numpy as np
array2=np.array([
    [
        [1,2,3,4,5,6],
        [2,3,4,5,6,7]
    ],
    [
        [4,5,6,7,8,8],
        [10,11,12,13,14,15]
    ]
    print(array2)
    for i in array2:
                for j in i:
                    for k in j:
                         print(k)
                
                

# view and copy in numpy 
import numpy as np
array=np.array([1,2,3,4,5,6])
print(array)
copy=copy.array()
print("Copy:",copy) # in copy if we change the elements from original array then there will be change in copy array
# view
view=veiw.array() # but for view ther will be no change, it prints the original array only
print("view:",view)

# join split and concatenate functions in numpy arrays
# join for 1d array
import numpy as np
array1=np.array([1,2,3,4,5,6])
array2=np.array([3,4,5,6,7,8])
print(array1)
print(array2)
new_array=np.concatenate((array1,array2))

# join for 2d array
import numpy as np
array3=np.array([
    [1,2,3,4,4,5,6],
    [4,5,6,7,87,8,9],
])
array4=np.array([
    [31,52,63,74,84,95,10],
    [43,55,66,778,897,98,99],
])
# print(array.shape)
# print(array.dtype)
# print(array.ndim)
new_array2=np.concatenate((array3,array4),axis=1)
new_array3=np.concatenate((array3,array4),axis=0)
print(new_array2)
print()
print(new_array3)


