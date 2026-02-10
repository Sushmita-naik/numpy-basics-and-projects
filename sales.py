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
