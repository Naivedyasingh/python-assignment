# 6.you're developing a program to analyze customer feedback ratings.write a python function to find the maximum rating from a tuple containing customer ratings

def max_rating(serves):
    highest_rating=0
    for customer_name,rating in serves:
        if highest_rating<rating:
            highest_rating=rating
    print(f"{customer_name} give highest rating {highest_rating}") 


customer_rating=(["rakesh",4.2],["ravaan",3.9],["salim",4.1],["arun sir",4.8])
max_rating(customer_rating)
