'''s=input("enter some:")
s1=s2=output=""
for i in s:
    if i.isalnum():
        s1=s1+i
    else:
        s2=s2+i
sorted_order=' '.join(sorted(s1))
print(s1)
print(s2) 
print(sorted_order)           
'''
s=input("enter some:")
s1=s2=output=""
for i in s:
    if i.isalnum():
        if i.isalpha():
           s1=s1+i
        else:
           s2=s2+i
sort1=''.join(sorted(s1)) 
sort2=''.join(sorted(s2)) 
print( sort1+str(sort2))   

    