def duplicate_string(str):
    result=""
    for i in str:
        if i not in result:
            result+=i
    print(result) 

def Palindrome(str):
    i=0
    j=len(str)-1
    while(i<j):
        if str[i]==str[j]:
            j-=1
            i+=1
        else:
            return False
    return True        

def Number_of_char(str):
    result={}
    for i in str:
        if i in result:   
            result[i]+=1  
        else:
            result[i]=1
    return result          

def reversed_string(str):
    words=str.split()
    reversed_str=' '.join(word[::-1] for word in words )
    return reversed_str
       
str1=input("Enter the string:")  
str2=input("Enter the sentence string:")
print(str2[::-1])
duplicate_string(str1) 
print(Palindrome(str1))
print(Number_of_char(str1))
print(reversed_string(str2))
