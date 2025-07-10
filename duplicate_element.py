s="abAbaba"
str=s.lower()
result=""
for ch in str:
    if ch not in result:
        result+=ch
print(result)        