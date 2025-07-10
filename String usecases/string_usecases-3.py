def validation_email(str):
    words=str.split()
    email=""
    for word in words:
        if '@' in word and '.' in word:
            word=word.strip(".,?!:;")

        addthess_index=word.find("@")
        dot_index=word.rfind(".")

        if addthess_index>0 and dot_index>addthess_index:
            email=email+word+','

    return email        
    


text= "please contact the collage tpo@gmail.com for the placement opportunity and also medicaps.ac.@gmail.com"
print(validation_email(text))