# 6.You're working on a program to manage a libary's book inventory. write a python function to remove a book from the inventory given its title

def remove_book_by_title(inventory,title_to_remove):
    for book in inventory:
        if book['title'].lower()==title_to_remove.lower():
            inventory.remove(book)
            print("Book is removed by inventory.")
    print("Book is not found in inventory")        


libary_inventory=[{'title':'harry Potter and the Sorcerer\'s stone','author':'J.K. Rowling','year':1997},{'title':'The hobbit','author':'J.R.R. Tolkien','year':1937},{'title':'1984','author':'George Orwell','year':1949}]
print(remove_book_by_title(libary_inventory,"harry Potter"))
