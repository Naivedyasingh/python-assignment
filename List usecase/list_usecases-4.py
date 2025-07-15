# 4.you're developing a to-do list application. How would you use the list in python to allow user to add,remove and mark task as complete
list1=[]
marking_task=[]
i=0
while True:
    
    print("Enter + if want to add the item")
    print("Enter - if want to remove the item")
    print('Enter = if want to see the task add and remove')
    print('Enter / if want to exit\n')
    input_value=input("Enter the input for task:")

    if input_value=='+':
        item=input('Enter item to add:')
        list1.append(item)
        print("Item added successfully.\n")
        i+=1
        marking_task.append(f"{i}.{item} add in the list.")
        
    elif input_value=='-':
        item=input('Enter item to remove:')  
        if item in list1:
            list1.remove(item)
            print("Item remove successfully.\n")
            i+=1
            marking_task.append(f"{i}.{item} remove from the list.")
        else:
            print("Item not found in the list.")    


    elif input_value=='=':
        print('\nHistory of task')
        for j in marking_task:
            print(j)
        print()    
    elif input_value=='/':
        print("Exiting the task manager.")
        break 
    else:
        print("Enter valid input.")        
    
