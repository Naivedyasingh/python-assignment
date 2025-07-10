test_string="Python Programming Pratice for Advanced Developers"
print(test_string[0:6])
print(test_string[1:-1:2])
print(test_string[0:-1:2])
print(test_string[0:-1:3])
print(test_string[5:15])
print(test_string[-10:])
print(test_string[::-1])
print(test_string[14:4:-1])
print(test_string[4:14:2])
substring="Advanced"
if substring in test_string:
    print(f"'{substring}' index '{test_string.index(substring)}'")
else:
    print('substring not found')    
print(test_string[-3:])    
print(test_string[-4:])
print(test_string[-4:-1])
print(test_string[::-3])