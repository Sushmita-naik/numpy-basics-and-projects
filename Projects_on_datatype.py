# import numpy as np
# bills=np.array(["199","349","499","999","1499"])
# print("The first bills are:",bills)
# int_bills=bills.astype(int)
# print("The integer bills are:",int_bills)
# print(int_bills.dtype)
# GST_bills=int_bills*0.18
# print("The GST of the bills are:",GST_bills)
# total_price=int_bills+GST_bills
# print("The total price after adding GST:",total_price)
# float_bills=total_price.astype(float)
# print(float_bills.dtype)

# import numpy as np
# Marks=np.array(["85.5", "90", "78.0", "88.5", "92"])
# float_Marks=Marks.astype(float)
# print("The floating marks are:",float_Marks)
# print("Tha marks after adding 5:",float_Marks+5)
# int_marks=float_Marks.astype(int)
# print("The integer marks are:",int_marks)
# avg=np.mean(int_marks)
# print("The average marks is:",avg)
# print(avg.dtype)

# import numpy as np
# array=np.array([10, 20.5, 30])
# print(array.dtype)
# new_array=array.astype(int)

import numpy as np
Sensors_data=np.array(["25", "30", "28", "32", "29"])
int_data=Sensors_data.astype(int)
print("The integer data of the sensors are:",int_data)
print("The data after adding 1 degree is:",int_data+1)
flota_data=int_data.astype(float)
print("The float data is:",flota_data)
devided_data=flota_data/2
print("The float data after dividing by 2:",devided_data)
print(devided_data.dtype)





