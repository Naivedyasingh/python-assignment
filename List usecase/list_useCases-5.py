# 5.You're developing a customer queue management sysytem for a service center. How would you use a list in python to manage the queue and serve customer?

def customer_queue_system():
    queue=[]

    while True:
        print('\n Service Center Queue ')
        print("1. Add customer to queue")
        print("2. Serve next customer")
        print("3. Show queue")
        print("4. Exit")

        choice=input("Enter your choice 1-4: ")
        if choice=='1':
            name=input("Enter customer name: ")
            queue.append(name)
            print(f"{name} added to the queue.")
        elif choice=='2':
            if queue:
                served=queue.pop(0)
                print(f"{served} has been served.")
            else:
                print("Queue is empty. No customers to serve.")    
        elif choice=='3':
            if queue:
                print("Current Queue:"," ".join(queue))
            else:
                print("Queue is empty.") 
        elif choice=='4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")           

customer_queue_system()
