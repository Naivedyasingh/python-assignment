# 1.Wite program to analyze customer data for retail store write a python program to find the unique set of cities where the customer reside

# set1=[{"company":"yash","city":"indore"},{"company":"tcs","city":"pune"},{"company":"yash","city":"indore"},{"company":"tcs","city":"pune"}]
# set2={i["city"] for i in set1}
# print(set2)

# 2.write program to manage cource enrollement for a university. write program to find the set of unique coures taken by a group of student

# set1=[{'name':'jj','coures':['maths']},{'name':'nsj','coures':['english']},{'name':'msj','coures':['maths']},{'name':['rsj'],'coures':['hindi']}]
# seen=set()
# duplicate=set()
# for std in set1:
#     for cour in std['coures']:
#         if cour in seen:
#             duplicate.add(cour)
#         else:
#             seen.add(cour)   

# unique_coures=seen-duplicate
# print(unique_coures)             



# 3.you're designing a program to analyze product review write a python program to find the set of unique positive words used in the reviews

# reviews=[
#     "the  product is amazing and very useful",
#     "excellent quality and great value for money",
#     "Good packing but average performance",
#     "Amazing service and good quality",
#     "Poor battery but excellent screen"
# ]
# positive_word={"amazing","excellent","great","good","useful","fantastic","superb","love"}

# all_word=[]
# for review in reviews:
#     words=review.split()
#     for word in words:
#         word_clean=word.lower().strip(".,")
#         all_word.append(word_clean)

        
# unique_positive=set()      
# for word in all_word:
#     if word in positive_word:
#         unique_positive.add(word)
# print(unique_positive)        


# 4.develop a program to analyze social media interaction write a python program to find the set of unique user who like or commented on a particular post

# post_interaction={"likes":["JJ","Msj","Nsj","SSj"],
#                   "comment":["Ysj","jsj","nsj","JJ"]}
# unique_post=set(post_interaction['likes']) | set(post_interaction['comment'])
# print(unique_post)


# 5.you're desinging a program to manage user prefered write a python program to find the set unique preferences across all users

user=[{'name':'jj','Preference':['play','learn','write','talk']},{'name':'nsj','Preference':['play','learn','write','talk','code','run']},{'name':'msj','Preference':['play','learn','write']},{'name':['rsj'],'Preference':['play','learn','write','fight','cook']}]
unique_preference=set()
for i in user:
    for j in i['Preference']:
        unique_preference.add(j)


print(unique_preference)        

