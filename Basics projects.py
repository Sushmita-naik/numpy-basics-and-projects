# import numpy as np
# marks=np.array([99,98,100,97,96])
# avg=np.mean(marks)
# print(avg)
# highest=np.max(marks)
# print(highest)
# lowest=np.min(marks)
# print(lowest)
# updated_marks=marks+5
# print("Marks after adding 5 grace marks:",updated_marks)
# above_avg=marks>avg
# count=np.sum(above_avg)
# print("student above avg:",count)


# import numpy as np
# temparature=np.array([36.4,54.3,45,42.8,33.01,25.6,27.4])
# avg=np.mean(temparature)
# print(avg)
# above_avg=temparature>avg
# print(above_avg)
# fahreniet=(temparature*1.8)+32
# print(fahreniet)

# import numpy as np
# expenses=np.array([1000,1500,200,400,800,960,650,470,380,357])
# total=np.sum(expenses)
# print(total)
# highest_spending=np.max(expenses)
# print(highest_spending)
# day_index=np.argmax(expenses)
# print("Highest spending day is",day_index)
# above_500=expenses>500
# count=np.sum(above_500)
# print("Days above 500 is",count)
# expenses[expenses>1000]=1000
# print("Expenses after limiting:",expenses)

# import numpy as np
# marks=np.array([
#     [80,90,100,65], #here axis 0 is column wise opration and axis 1 is row wise operation
#     [34,67,89,22],
#     [99,97,76,45]
# ])
# print(marks.shape)
# student_total=np.sum(marks,axis=1)
# print("Total per student:",student_total)
# subject_total=np.mean(marks,axis=1)
# print("Average per each subject is",subject_total)
# overall_avg=np.mean(marks)
# print("The overall average is:",overall_avg)
# top_student=np.argmax(student_total)
# print("Top student index:",top_student)

# import numpy as np
# step_walk=np.array([10500,4500,6500,1200,5500,8000,7000,1230,741,852,369,456,1237,465,746,841,236,5987,4561,2356,4579,145,789,456,125,555,963,789,111,444])
# total_steps=np.sum(step_walk)
# print("The total steps are:",total_steps)
# avg_steps=np.mean(step_walk)
# print("The average step is",avg_steps)
# above_10000=step_walk>10000
# count=np.sum(above_10000)
# print("the total which are having more than 10000 steps are",count)
# step_walk[step_walk<2000]=2000
# print("Steps after replacing 2000",step_walk)
# best_day=np.argmax(step_walk)
# print("The best day",best_day)

# import numpy as np
# sale_data=np.array([
#     [500,600,700,800,350,850,444],
#     [333,5605,8900,145,745,2033,456],
#     [7707,231,2580,147,369,8502,741],
#     [7809,456,123,357,159,2480,156]
# ])
# total_sales_per_week=np.sum(sale_data,axis=1)
# print("The total sales according to each week is:",total_sales_per_week)
# total_sales_per_day=np.sum(sale_data,axis=0)
# print("The total sales per day across all weeks are:",total_sales_per_day)
# overall_total=np.sum(sale_data)
# print("The overall total monthly sales",overall_total)
# highest_total=np.argmax(total_sales_per_week)
# print("The week which is having highest total sales is:",highest_total)
# sale_data[sale_data>2000]=2000
# print("The sales after replacing 2000",sale_data)


import numpy as np
attendence_data=np.array([
    [1,0,1,1,1,0,1],
    [0,0,1,0,1,1,1],
    [1,1,1,1,1,0,0],
    [0,0,0,0,1,1,1],
    [1,1,1,0,0,0,1]
])
total_days_present_for_each_student=np.sum(attendence_data,axis=1)
print("The total days present for each student is",total_days_present_for_each_student)
student_present_each_day=np.sum(attendence_data,axis=0)
print("The students were present in each day is:",student_present_each_day)
totals=np.sum(attendence_data,axis=1)
highest_attendence=np.argmax(totals)
print("The student which is having highest attendence is:",highest_attendence)
less_than_3_days=totals<3
count=np.sum(less_than_3_days)
print("the student are having attendance less than 3 days are:",count)
totals[totals<2]=2
print("the student attendance below 2 days are replacing",totals)