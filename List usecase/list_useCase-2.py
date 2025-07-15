#you're developing a task management application how oud you use list to allow users to add,remove,view task
print("Welcome to task management system")

tasks=[]

while True:
    print("Enter 1 for Add task")
    print("Enter 2 for remove task")
    print("Enter 3 for view task")
    print("Enter 4 for Exit")

    choice=input("Enter you choice (1-4) for management:")

    if choice=='1':
        add=input("Enter the task to add:")
        tasks.append(add)
        print(f"Task '{add}' added.")
    elif choice=='2':
        remove_ele=input("Enter the value to remove from task ")
        if remove_ele in tasks:
           tasks.remove(remove_ele)
        else:
            print("Enter the wrong elemenet")
    elif choice=='3':
        if tasks:
            print("your tasks")
            for i,task in enumerate(tasks,1):
                print(f"{i}.{task}") 
        else:
            print("no task is in data.")       
    elif choice=='4':
        print("Exiting task Manager.")
        break
    else:
        print("Enter the invalid input. please enter the correct one")                


