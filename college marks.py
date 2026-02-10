# import numpy as np
# college_marks=np.array([
#     [
#         [70,88,48,68],
#         [91,92,83,84],
#         [74,85,96,67],
#         [48,79,53,85],
#         [65,37,29,61]
#     ],
#     [
#         [81,84,86,87],
#         [94,95,96,57],
#         [79,79,86,94],
#         [51,61,72,93],
#         [72,85,46,74]
#     ],
#     [
#         [61,82,93,65],
#         [67,78,98,99],
#         [80,79,65,52],
#         [100,51,83,34],
#         [71,68,75,64]
#     ]

# ])
# total_marks_per_class=np.sum(college_marks,axis=0)
# print("The total marks per each class",total_marks_per_class)
# average_per_subjetc=np.mean(college_marks,axis=2)
# print("The average marks per subject is:",average_per_subjetc)
# student_totals=np.sum(college_marks,axis=2)
# best_student=np.argmax(student_totals,axis=1)
# print("Best student index in each class:",best_student)

import numpy as np

sales = np.array([
    [
        [500, 300, 200],
        [600, 400, 350],
        [550, 320, 250],
        [700, 500, 450],
        [650, 480, 300],
        [720, 510, 390],
        [800, 600, 500]
    ],
    [  
        [400, 250, 150],
        [450, 300, 200],
        [500, 350, 300],
        [550, 400, 350],
        [600, 450, 400],
        [650, 500, 450],
        [700, 550, 500]
    ]
])
total_sales_per_shops=np.sum(sales,axis=(1,2))
print("The total sales for shop is:",total_sales_per_shops)
total_sales_per_products=np.sum(sales,axis=(0,1))
print("the total sales per product is:",total_sales_per_products)
overall_sales=np.sum(sales)
print("The overall sales:",overall_sales)
highest_sale=np.argmax(total_sales_per_shops)
print("The shop which is having highest sold is:",highest_sale)
