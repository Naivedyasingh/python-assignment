# 5.you're working on a program to process customer orders.write a pyhotn function to calculate the total cost of an order given tuple representing the item price and quantity
def total_amount(order):
    for item,price,quantity in order:
        total=0
        total=price*quantity
        print(f"{item} value is: {total}")

order=[('milk',20,10),('tea',30,30),('sugar',100,5)]
total_amount(order)