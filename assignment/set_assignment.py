# 1.Write a Program to check if a subset of another set

# a={1,2,7,4,5}
# b={1,2,3,4,5,6}

# for i in a:
#     if i not in b:
#         print(False)
#         break
# else:
#     print(True)  

# 2.Write a progrm to remove the duplicate element form given list of strings and return a list of unique string use the python set data type.

# list_string=["the","people","are","good","and","the","value","that","people"]
# list_qnique=set(list_string)
# print(list(list_qnique))


# 3.Write a program to find the union,intersection,symmetric,difference of the two set.
# a={1,2,3,4,5,6,7}
# b={2,5,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))


# 4.write a program to creste a symmetric difference

# a={1,2,3,4,5,6,7}
# b={2,5,8}
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))

  
# 5.Write a program to count the number of vowels sets in given string

str="hello worlda"
vowels_set={'a','e','i','o','u'}
count=0
for i in str:
    if i in vowels_set:
        count+=1
print(count)        