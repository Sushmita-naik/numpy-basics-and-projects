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


