'''

# 1.Write program to print true if all character is the string isdigit else false
str=input("Enter the anything:")
if str.isdigit():
    print(True)
else:
    print(False)

'''


'''
 # 2.Write a program to create a new string made of the first middle, and last character of each input string

str1="python"
str2="dajngo"
n=len(str1)//2-1
m=len(str2)//2-1

first=str1[0]+str2[0]
print(first)
midde=str1[n]+str2[m]
print(midde)
last=str1[-1]+str2[-1]
print(last)
full=first+midde+last
print(full)
'''

'''
# 3.Write a program to append the nw string in the middle
str1='helloopython'
str2='world'
mid=len(str1)//2
new_string=str1[:mid]+str2+str1[mid:]
print(new_string)
'''


'''

# 4.write a program to arrange string character such that lowercase letter should come first
input_string='PythoNwaS12Gn'
lower=""
upper=""
for i in input_string:
    if i.islower():
        lower+=i
    else:
        upper+=i

result=lower+upper
print(result)        

'''


'''

# 5. Write a program to count the all letters digits and special character from the string
str="P@#yn26at^&i5ve"
chars=Digits=Symbols=0

for i in str:
    if i.isnumeric():
        Digits=Digits+1
    elif i.isalpha():
        chars=chars+1
    else:
        Symbols=Symbols+1        

print("Characters are",chars)
print("Digits are",Digits)
print("Symbols are",Symbols)

'''
'''

# 6.Write a program to test the balance test


s1="Foi"
s2="PythonFastAPI"
if len(s1)>len(s2):
    print(False)
else:
    for i in s1:
        if i not in s2:
           print(False)
           break   
    else:
        print(True)


        '''


'''
# 7. write  a program to count occurence of all character within a string 

str1="Pythonpy"
result=""

for i in str1:
    if i not in result:
        count=0
        for n in str1:
            if i==n:
                count+=1
        print(f"{i} : {count}")    
        result+=i     

        '''

'''


# 8.Write a program to find the last position of a substring in a given string

str1="How much wood would a woodchunk chuck if a woodchuck could chuck wood?"

substring="chuck"
last_string=str1.rfind(substring)
print(last_string)

'''


'''
# 9.write a program to split a given string on hyphens and display each substring
text="Violet-Indigo-Blue-Green-Yellow-Orange-Red"
word=text.split("-")
print(word)

'''
# 10. Write a program to remove special symbols/punction from a string
text="Hello, World! Welcome to python @ 2025"
new_string=""
for i in text:
    if i.isalnum() or i.isspace():
        new_string=new_string+i
print(new_string)        
