
import numpy as np
hospital_data=np.array([
    [
        [98.6, 99.1, 100.2, 97.9],
        [99.0, 98.7, 101.0, 98.5],
        [100.1, 99.5, 98.8, 97.6],
        [98.4, 100.3, 99.2, 98.9],
        [97.8, 98.6, 99.9, 100.5],
        [99.4, 98.2, 97.5, 100.0],
        [98.9, 99.7, 98.3, 97.4]
    ],
    [
        [99.5, 100.1, 98.7, 97.8],
        [98.9, 99.2, 100.4, 98.6],
        [97.6, 98.5, 99.3, 100.0],
        [99.8, 98.1, 97.9, 100.2],
        [98.4, 99.6, 100.3, 97.7],
        [97.5, 98.8, 99.0, 100.6],
        [99.1, 98.3, 97.4, 100.1]
    ],
    [
        [100.2, 99.4, 98.6, 97.9],
        [98.7, 100.5, 99.1, 97.8],
        [99.3, 98.2, 100.0, 97.6],
        [97.5, 99.9, 98.4, 100.3],
        [98.8, 97.7, 99.6, 100.4],
        [100.1, 98.3, 97.9, 99.2],
        [97.6, 100.0, 98.5, 99.7]
    ]
])
ward_avg=np.mean(hospital_data,axis=(1,2))
print("Average temparature of ward  is:",ward_avg)
daily_avg=np.mean(hospital_data,axis=(0,2))
print("The daily avarege temparature is:",daily_avg)        #axis 0 is ward and, axis 1 is day, and axis 2 is patient
overall_average=np.mean(hospital_data)
print("The overall average of the hospital is:",overall_average)
highest_avg=np.argmax(ward_avg)
print("Ward with highest average is:",highest_avg+1)
fever_cases=np.sum(hospital_data>101)
print("The number of fever cases:",fever_cases)
hospital_data[hospital_data>104]=104
print("Replacing safety cap:",hospital_data)

