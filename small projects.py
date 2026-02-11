# import numpy as np
# weekly_tracker=np.zeros(7)
# print("empty tracker is:",weekly_tracker)
# # weekly_tracker[:]=[2,3,4,5,6,2,1]
# # print(weekly_tracker)
# weekly_tracker[0]=2
# weekly_tracker[1]=3
# weekly_tracker[2]=4
# weekly_tracker[3]=5
# weekly_tracker[4]=6
# weekly_tracker[5]=2
# weekly_tracker[6]=1
# print("Weekly tracker is:",weekly_tracker)
# total=np.sum(weekly_tracker)
# print("The total study hours are:",total)
# average=np.mean(weekly_tracker)
# print("The average study hours are:",average)
# best_day=np.argmax(weekly_tracker)
# print("the best study hour is:",best_day)

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