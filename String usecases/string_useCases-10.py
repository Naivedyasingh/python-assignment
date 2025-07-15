# 10.you're developing a text preprocessing tool that  requires identify the most common word in the given text. Implement a python  function to find the most frequent word in the text string excluding common stop word such as the ,is,and etc.
text="yash technologies is walking distance from my home and they why i am come early in the company so that i can spend the more time in the company can can The The The The"
exclude=['the','is','and']
words=text.split(" ")
maxi=0
str=""
for i in words:
    if i.lower() not in exclude:
        cnt=words.count(i)
        if cnt>maxi:
            maxi=cnt
            str=i
    else:
        pass
print(f"{str.capitalize()} come {maxi} times in the text")  
         
