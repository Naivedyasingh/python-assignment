# # person={'name':'jessia','country':'usa','telephone':1991}
# # print(person.items())
# # print(person.get('name'))
# # person['name']='nsj'
# # print(person['name'])
# # del person
# # # for key in person:
# # #     print(key,":",person[key])
# # # for key,value in person.items():
# # #     print(key,value) 
# # 
# # 
# # 
# word=input("enter the string")

# # item={}
# # for x in word:
# #     if x in item:

# #        item[x]+=1
# #     else:
# #         item[x]=1   
# # sorted_dict=dict(sorted(item.items()))
# # print(sorted_dict)    


# str1=input("enter the string:")
# vowels={'a','e','i','o','u'}

# vowel={}
# cont={}
# for i in str1:
#     if i in vowels:
#         if i in vowel:
#             vowel[i]+=1
#         else:
#             vowel[i]=1
#     else:
#         if i not in cont:
#             cont[i]=1
#         else:
#             cont[i]+=1            
# print(f"vowel and their count:{vowel} and cont count:{cont}")

     
num=int(input("Enter the number student data:"))
data={}
for i in range(num):
    name=input("Enter the name of studet:")
    marks=int(input("Enter the marks:"))
    data[name]=marks
print(data)    