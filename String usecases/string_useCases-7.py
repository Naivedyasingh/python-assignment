# write a python program to process user input and implement python function to find the most frequent word in a given tect string
# str=input("Enter the string")
# max=0
# most_frequent=""
# for i in str:
#     count=0
#     for j in str:
#         if i==j:
#             count+=1

#     if count>max:
#         max=count
#         most_frequent=i

# print(most_frequent)         
# 
# 



str=input("Enter the string")
max_count=0
most_frequent={}
for char in str:
    most_frequent[char]=most_frequent.get(char,0)+1
max_count=max(most_frequent.values())

most_frequent_chars=[char for char, count in most_frequent.items() if count==max_count]
print(most_frequent_chars)

