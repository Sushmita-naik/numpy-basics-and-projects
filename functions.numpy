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
