# # 1.Write a python program merge two tuples and remove duplicates
# tup1=(1,2,3,4,51,2,3,1)
# tup2=(51,56,1,46,3,5)
# tup3=tup1+tup2
# unique_element=[]
# for i in tup3:
#     if i not in unique_element:
#         unique_element.append(i)
# result=sorted(tuple(unique_element))
# print(result)        


# 2.write a program to convert the tuple of interger to a tuple string
# tup=(1,2,3,4,5,6,7,8)
# tup1=tuple(str(i) for i in tup)
# print(tup1)

# 3.write a program find the frequency of each element in tuple
# tup=(1,2,2,32,3,2,1,3,2,23,3,3,2,2,5,432,2)
# printed=()
# for i in tup:
#     if i not in printed:
#         freq=tup.count(i)
#         print(f"{i}:{freq}")
#         printed+=(i,)


# 4.Write a program find the difference  between two tuple
# tup1=(1,2,3,4,5)
# tup2=(2,4,6)
# tup3=()
# for i in tup1:
#     if i not in tup2:
#         tup3+=(i,)
# print(tup3)


# 5.write program to find the second largest element
# tup=(1,2,10,8,9)
# second_largest=0
# largest=tup[0]
# for i in tup:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif second_largest<i<largest:
#         second_largest=i   
# print(second_largest)        



# 6.write a program to check if tuple is a subset of other tuple
# tup1=(1,2,7)
# tup2=(1,2,3,4,5,6)
# result=all(i in tup2 for i in tup1)
# print(result)

# 7.write a program to extract tuples having k digit elements k=2
# tup=[(47,23),(3,78),(22,53),(121,45),(7,)]
# k=2
# result=[i for i in tup if all(len(str(abs(x)))==k for x in i)]
# print(result)


#8.write a program to sort the tuple by second elements

# value=[('for',2),('in',7),('this',1),('it',0)]
# sorted_tup=sorted(value,key=lambda x:x[1])
# print(sorted_tup)


# 9.Remove an element from a tuple
# tup=(1,2,3,4,5,6)
# remove_ele=3
# tup2=()
# for i in tup:
#     if i!=remove_ele:
#         tup2+=(i,)

# print(tup2)    



# 10.Write a program to compute the element-wise sum is given tuples
tup1=(1,2,34,5)
tup2=(2,3,4,7)
tup3=(3,44,66,7)
sum_result=[]
for i in range(len(tup1)):
    total=tup1[i]+tup2[i]+tup3[i]
    sum_result.append(total) 
print(tuple(sum_result))


# result=tuple(a+b+c for a,b,c in zip(tup1,tup2,tup3))
# print(result)
