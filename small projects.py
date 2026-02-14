import numpy as np
weekly_tracker=np.zeros(7)
print("empty tracker is:",weekly_tracker)
 weekly_tracker[:]=[2,3,4,5,6,2,1]
 print(weekly_tracker)
weekly_tracker[0]=2
weekly_tracker[1]=3
weekly_tracker[2]=4
weekly_tracker[3]=5
weekly_tracker[4]=6
weekly_tracker[5]=2
weekly_tracker[6]=1
print("Weekly tracker is:",weekly_tracker)
total=np.sum(weekly_tracker)
print("The total study hours are:",total)
average=np.mean(weekly_tracker)
print("The average study hours are:",average)
best_day=np.argmax(weekly_tracker)
print("the best study hour is:",best_day)

import numpy as np
Balance_analyzer=np.zeros(10)
print(Balance_analyzer)
daily_deposits=np.linspace(1000,10000,10)
print("The daily deposits are:",daily_deposits)
print("Adding bonus 500 to each account:",daily_deposits+500)
total=np.sum(daily_deposits)
print("The total balance is:",total)
avarage_balance=np.mean(daily_deposits)
print("The avg balance is:",avarage_balance)
days_balance=daily_deposits>5000
count=np.sum(days_balance)
print("The balance which is > 5000 is:",count)
daily_deposits[daily_deposits>10000]=10000
print("The daily deposits replaced by 10000:",daily_deposits)


# arithmatic operators
import numpy as np
salary=np.array([25000,30000,28000,35000,40000])
new_salary=salary+(salary*0.10)
print("Salary after adding 10% :",new_salary)
deduction_salary=new_salary-(new_salary*0.05)
print("Salary after adding 5% discount:",deduction_salary)
total1=np.sum(deduction_salary)
print("The total salary amount is from deduction salary is :",total1)
total2=np.sum(salary)
print("The total salary amount is from salary is:",total2)
avg=np.mean(salary)
print("the avg salary amount is:",avg)
extra_salary=total1-total2
print("The comapany is paying extra money that is :",extra_salary)

import numpy as np
Marks=np.array([45,60,72,88,95])
new_marks1=Marks+5
print("The new marks after adding 5 grace marks is:",new_marks1)
total=np.sum(Marks)
print("The total marks is:",total)
new_marks2=Marks*1.05
print("The marks after multiplying 1.05 is:",new_marks2)
percentage=(Marks/total)*100
print("The percentage of the marks is:",percentage)

# STOCK PRICE ANALYZER
import numpy as np
price=np.array([100,105,98,110,115,120])
profit=price-price[0]
print("Profit compared to day 1:",profit)
projected=price*1.05
print("5% growth projection:",projected)
difference=price[1:]-price[:-1]
print("The daily price change is:",difference)
overall_growth=((price[-1]-price[0])/price[0]*100)
print("The overall % growth:",overall_growth)
minimum_marks=Marks.min()

# arithmatic functions
import numpy as np
steps=np.array([4500,8000,6200,10000,3000,7500,9000])
print("The minimum step is:",min(steps))
print("The maximum step is:",max(steps))
print("the lowest steps of the day is:",np.argmin(steps))
print("the highest step of the day is:",np.argmax(steps))
print("the total steps are:",np.cumsum(steps))
print("the square root of the steps are:",np.sqrt(steps))
print("The minimum mark is:",minimum_marks)
maximum_marks=Marks.max()
print("the maximum marks is:",maximum_marks)

import numpy as np
items=np.array([120,150,90,200,170,80,220,160,140,130])
print("The best production is :",np.max(items)," and the day is:", np.argmax(items))
print("The worst production is :",np.min(items)," and the day is:", np.argmin(items))
print("the total cost of the prices are:",np.cumsum(items))
print("The sqaure root of the production value is:",np.sqrt(items))
max_item=np.max(items)
print("The maximum value of the item is:",max_item)
difference=max_item-items
print("The difference from maximum is:",difference)
total_value=np.sum(items)
print("the total values of the items are:",total_value)
percentage=(items/total_value)*100
print("The percentage contribution is:",percentage)
avg=np.mean(items)
above_avg=items>avg
print("the days above average is:",above_avg)


# shape and reshape
import numpy as np
student_seat=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60])
reshape_seats=student_seat.reshape(6,10)
print("The student seat after replacing is:\n",reshape_seats)
print(reshape_seats.ndim)
print(reshape_seats.shape)
reshape_3d=reshape_seats.reshape(3,2,10)
print("The 3d array is:\n",reshape_3d)

import numpy as np
values=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
reshape=values.reshape(4,4)
print("The image after reshaping into 4x4:\n",reshape)
reshape_2=reshape.reshape(2,2,4)
print("The dimenssion is :",reshape.ndim)
print("The image after reshaping 2x2x4:\n",reshape_2)
print("The image dimension after reshaping:\n",reshape_2.ndim)

import numpy as np
sales_cube=np.arange(1,61)
print("The sales cube is:\n",sales_cube)
reshape=sales_cube.reshape(3,4,5)
print("The sales 3d array is:\n",reshape)
print(reshape.ndim)
total_elem=np.sum(reshape)
print("The total elements are:\n",total_elem)
print(reshape.ndim)


import numpy as np
records=np.arange(1,121)
print("The hospital records are:\n",records)
reshape=records.reshape(2,3,4,5)
print("The record after reshaping is:\n",reshape)
print("The shape is:\n",reshape.shape)
print("The dimenssion is:",reshape.ndim)
print("Building 1, Floor 2 data:\n",reshape[0, 1])


import numpy as np
marks=np.arange(1,251)
marks_2d=marks.reshape(50,5)
print(marks_2d)
subject_avg=np.mean(marks_2d,axis=0)
print("The subject wixe average is:",subject_avg)
student_total=np.sum(marks_2d,axis=1)
print("The student wise total is:",student_total)
topper=np.argmax(marks_2d)
print("The topper is:",topper)
hardest_subject=np.argmin(subject_avg)
print("The hardest subject is:",hardest_subject)
weakest_subject=np.argmin(subject_avg)
print("The weakest subject is:",weakest_subject)
print("Adding grace 5 marks to the weakest subject:",weakest_subject+5)
percentage=(student_total/500)*100
print("The percentage for each student is:",percentage)
rank_order=np.argsort(-percentage)
print("Ranking order (best to worst):",rank_order)

# weather data analyzer
import numpy as np
temparature=np.arange(1,121)
temparature_2d=temparature.reshape(30,4)
print("Temaparature is:\n",temparature_2d)
avg_temp=np.mean(temparature_2d,axis=1)
print("The average temparature is:",avg_temp)
time_avg=np.mean(temparature_2d,axis=0)
hottest_time=np.argmax(time_avg)
print("The hottest time of day index is:",hottest_time)
coldest=np.min(temparature_2d)
coldest_idx=np.argmin(temparature_2d)
print("Coldest temparature is:",coldest)
print("Position of the temparature is:",coldest_idx)
trend=np.cumsum(avg_temp)
print("The cumulative trend :",trend)
temp_f=(temparature_2d*9/5)+32
print("Temparature in fahrenhiet is:\n",temp_f)
sin_wave=np.sin(temparature_2d)
print("Simulated pattern:\n",sin_wave)

# electricity consumption
import numpy as np
electricity_consumption=np.arange(1,8641)
electricity_consumption3d=electricity_consumption.reshape(12,30,24)
print("The electricity record of the house is:\n",electricity_consumption3d)
total_electricty_per_month=np.sum(electricity_consumption3d,axis=(1,2))
print("the total electicity consumed per month is:",total_electricty_per_month)
daily_total=np.sum(electricity_consumption3d,axis=2)
avg_consumption=np.mean(daily_total,axis=(1,2))
print("the average electricity consumed per month is:",avg_consumption)
peak_usage_hour=np.argmax(electricity_consumption3d)
month,day,hour=np.unravel_index(peak_usage_hour,electricity_consumption3d.shape)
print("the peak usage at = month:",month,"Day",day,"Hour:",hour)
most_electricity=np.argmax(total_electricty_per_month)
print("most electricity consumed month is:",most_electricity)
bill_amount=electricity_consumption3d*6
print("The total bill amount is:",bill_amount)
monthly_bill_amount=total_electricty_per_month*6
print("Monthly bill amount is:",monthly_bill_amount)
daily_avg=np.mean(daily_total)
highest_usage_days=daily_total>daily_avg
print("The highest usage days are:",highest_usage_days)
count=np.sum(highest_usage_days)
print("The number of high usage days:",count)




