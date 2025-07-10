str="Duugu Khushi sulabh"
word=str.split(" ")
reversed_string="" 
for i in range(len(word)-1,-1,-1):
    rev=''.join(reversed(word[i]))
    reversed_string+=rev+" "
print(reversed_string)    