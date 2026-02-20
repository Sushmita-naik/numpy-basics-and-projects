# functions in numpy arrays
# 1.search array
import numpy as np
array=np.array([12,3,4,5,5,6,54,4,43,3,32])
y=np.where(array==12)
print(y)
z=np.where((array%2)==0)
print(z)
x=np.where((array/2)==0)
print(x)

# for 2d array
array2=np.array([
    [12,3,4,5,6,6,7],
    [56,67,8,764,23,12,67]
])
find=np.where(array2==6)
print(find)
find_1=np.where((array2 % 2==0))
print(find_1)

# search sorted array 
import numpy as np
array=np.array([1,2,3,4,5,6,7])
print(array)
y=np.searchsorted(array,3)
print(y)
print(np.searchsorted(array,3,side="left"))
print(np.searchsorted(array,3,side="right"))
array=np.array([1,2,3,3,3,3])
print(array)
print(np.searchsorted(array,3,side="right"))
print(np.searchsorted(array,3,side="left"))
print(np.searchsorted(array,3,side="right"))

# Filter functions in numpy 
import numpy as np
array=np.array([1,2,3,4])
print(array)
f=[True,False,True,False]
new_array=array[f]
print(new_array)

array = np.array([5, 10, 15, 20])
mask = [False, True, False, True]
print(array[mask])

# arithmatic functions in numpy
# 1. Shuffle function for 1d array
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,10])
print("Array before shuffuling is:\n",array)
np.random.shuffle(array)
print("The array after shuffle is:\n",array)

# for 2d array
import numpy as np
array2=np.array([
    [1,2,3,4,5,5],
    [6,7,8,8,10,11],
    [11,22,33,44,55,66]
])
print("the array before shuffuling :\n",array2)
np.random.shuffle(array2)
print("The array after shuffuling:\n",array2)

# unique function in numpy
# for 1d array
import numpy as np
array=np.array([1,2,1,2,33,4,5,6,5,4,3,3,2,1,67,68,564,67,86,78475,857467])
print("The original array is:\n",array)
unique_array=np.unique(array)
print("The unique array is:\n",unique_array)

# for 2d array
import numpy as np
array=np.array([
    [1,2,3,4,2,1,3,5,6,7,5,8,7,8], # same for 3d array also
    [1,2,3,4,5,6,7,8,9,1,2,4,5,2]
])
print(array)
print()
x=np.unique(array)
print(x)

# resize function in numpy
# for 1d array
import numpy as np
array=np.array([1,2,3,4,5,6,67,34])
y=np.resize(array,(4,4)) # it does not care about the how much elements it is holding from past if we give the resize array size as more than the elements which are present in org array it does not care about that, it will repeat the array elements
print(y)

# flatten function in numpy # it is used to convert the 2d array to 1d array
print(y.flatten(order="F"))
# ravel
print(np.ravel(y,order="F"))
print(np.ravel(y,order="A"))
print(np.ravel(y,order="C"))
print(np.ravel(y,order="K"))
