# 9.write a python program to find the user name from the given email.

email="naivedyasingh25@gmail.com"
user_name=email.split('@')[0]
user=""
for i in user_name:
    if i.isalpha():
        user+=i
    else:
        break    

print(user)