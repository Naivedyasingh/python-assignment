# you are building a python program to process text data write a python function to find the longest substring of consective vowel in a given string

str="helloworld fulinjoyment and work it au"
vowels=set('aeiouAEIOU')
longest=""
current=""
for i in str:
    if i in vowels:
        current+=i
        if len(current)>len(longest):
            longest=current
    else:
        current=""  

print(longest)             