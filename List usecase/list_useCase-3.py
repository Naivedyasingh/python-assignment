# 3.write program to calculate the avg of the collage student grades.How could use list in python 

number_std=int(input("Number of students:"))
list1=[]
for i in range(number_std):
    list1.append(float(input(f"Enter the grade of the student {i+1}:")))

avg=sum(list1)/number_std
print(f"Average of the student is:{avg}")    