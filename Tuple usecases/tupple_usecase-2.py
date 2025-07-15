# 2.you're desinging a program to manage inventory levels. Write a python function to check if a tuple representing as item stock status indicates low stock
def low_stock(tup):
    threshold=10
    name,quantity=tup
    if quantity<threshold:
        print(f"low stock of {name} ")
    else:
        print(f"{name} have sufficient stock")    



item_name=input("Enter the name of item to check the stock: ")
item_quantity=int(input("Enter the quantity:"))
tup=(item_name,item_quantity)
low_stock(tup)

   
