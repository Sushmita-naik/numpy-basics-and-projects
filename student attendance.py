
# import numpy as np
# attendence_data=np.array([
#     [1,0,1,1,1,0,1],
#     [0,0,1,0,1,1,1],
#     [1,1,1,1,1,0,0],
#     [0,0,0,0,1,1,1],
#     [1,1,1,0,0,0,1]
# ])
# total_days_present_for_each_student=np.sum(attendence_data,axis=1)
# print("The total days present for each student is",total_days_present_for_each_student)
# student_present_each_day=np.sum(attendence_data,axis=0)
# print("The students were present in each day is:",student_present_each_day)
# totals=np.sum(attendence_data,axis=1)
# highest_attendence=np.argmax(totals)
# print("The student which is having highest attendence is:",highest_attendence)
# less_than_3_days=totals<3
# count=np.sum(less_than_3_days)
# print("the student are having attendance less than 3 days are:",count)
# totals[totals<2]=2
# print("the student attendance below 2 days are replacing",totals)


import numpy as np
college_marks=np.array([
    [
        [70,88,48,68],
        [91,92,83,84],
        [74,85,96,67],
        [48,79,53,85],
        [65,37,29,61]
    ],
    [
        [81,84,86,87],
        [94,95,96,57],
        [79,79,86,94],
        [51,61,72,93],
        [72,85,46,74]
    ],
    [
        [61,82,93,65],
        [67,78,98,99],
        [80,79,65,52],
        [100,51,83,34],
        [71,68,75,64]
    ]

])
total_marks_per_class=np.sum(college_marks,axis=0)
print("The total marks per each class",total_marks_per_class)
average_per_subjetc=np.mean(college_marks,axis=2)
print("The average marks per subject is:",average_per_subjetc)
student_totals=np.sum(college_marks,axis=2)
best_student=np.argmax(student_totals,axis=1)
print("Best student index in each class:",best_student)
