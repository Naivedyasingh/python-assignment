#you're conducting a survey and need to store the responses from participants how would you utlizie a list in py to amamanage thes responses
Number_of_response=int(input("Enter the who much response you have:"))
reponses=""
all_responses=[]
for i in range(0,Number_of_response):
    reponses=input(f"Enter the response {i+1} :")
    all_responses+=[reponses]
print(all_responses)    