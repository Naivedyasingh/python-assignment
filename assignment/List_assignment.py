'''
# 1.write a program to Interchange first and the last element of in a List
list1=[1,2,3,4,5,6,7,8,9]
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)
'''

'''
# 2.Write a python program to remove multiple empty string from list of string
list_string=["hello","world","","python","","coding"]
list_string=[i for i in list_string if i != ""]
for i in list_string:
    if i =="":
        list_string.remove()
print(list_string)

'''


'''

# 3.Write a python program to half the list and store the element in two different list
list1=[12,3,42,4,23,46,267,75,467,56,2,4,6,8]
mid=len(list1)//2
list2=list1[:mid]
list3=list1[mid:]
print(list2)
print(list3)
'''
'''

# 4.Remove all occurence of an element from a list
list1=[1,2,3,2,4,2]
occurence=2
list2=[x for  x in list1 if x!=occurence]
print(list2)
'''
'''

# 5.Write a python program to remove the negative value from a list with filter() function
list1=[1,-1,-2,3,3,1,2,-2,9]
positive_list=[]
for i in list1:
    if i>0:
        positive_list.append(i)
print(positive_list) 
'''

# # 6.Write a python program to count the number of string where the string length is 2 or more and the first and last character are same from a given list of string
# list1=['abc','aba','xyz','1221','xyx']
# count=0
# for i in list1:
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
# print(count)


# 7.write a program to shuffle and print a specified list 
# import random 
# animals=['Cat','Dog','Elephant',"Fox","Tiger","Lion","Ponda"]
# animals1=set(animals)
# random.shuffle(animals)
# print(animals)

# # 8.write a program to remove repetitive items from a list
# list1=[1,2,3,3,12,1,2,1,21,'list','tuple','list']
# list2=[]
# for i in list1:
#     if i not in list2:
#         for j in list1:
#             if i==j:
#                 list2.append(i)
#                 break

# print(list2) 
# 


# 9.Find the longest word in a list words
list1=["the","Coding","12212","programing","programin1"]
max=0
result=[]
for i in list1:
    if len(i)>max:
        max=len(i)
for j in list1:
    if len(j)==max:
        result.append(j)
print(result)        