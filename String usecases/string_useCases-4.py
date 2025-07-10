def check_lower(str):
    for i in str:
        if i.islower():
            return True
    return False

def check_upper(str):
    for i in str:
        if i.isupper():
            return True
    return False


def check_digit(str):
    for i in str:
        if i.isdigit():
            return True
    return False


def check_special(str):
    for i in str:
        if not i.isalnum():
            return True
    return False



def strong_password(str):
    if len(str)<=8:
        return "Enter the minimum 8 character"
    if not check_lower(str):
        return "Enter One lower character"
    if not check_upper(str):
        return "Enter One upper character"
    if not check_digit(str):
        return "Enter One digit character"
    if not check_special(str):
        return "Enter One special character"
    
    return "It was an strong password"


str=input("Enter the password to check it was an strong or not :")
print(strong_password(str))

