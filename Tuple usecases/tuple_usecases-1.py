# 1.build a program to store information about employee write a python function to create a tuple representing an employee given their name age and departement
def create_empl(start,name,age,department):
    return (start,name,age,department)


def input_employee(n):
    employee=[]
    start_id=101
    for i in range(n):
        print("Enter the employee detail {i+1}:")
        name=input("Enter the name of employee:")
        age=int(input("Enter the age of employee:"))
        department=input("Enter the department of employee:")
        emp=create_empl(start_id+i,name,age,department)
        employee.append(emp)
    return employee    

n=int(input("Enter the number of employee:"))
employee_list=input_employee(n)

for i in employee_list:
    print(employee_list)

