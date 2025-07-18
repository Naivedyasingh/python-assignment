# # import re
# # import getpass

# # # In-memory user store
# # users = {}

# # # ✅ Email validation
# # def is_valid_email(email):
# #     pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
# #     return re.match(pattern, email)

# # # ✅ Password strength checker
# # def is_strong_password(password):
# #     return (len(password) >= 8 and
# #             re.search(r"[A-Z]", password) and
# #             re.search(r"[a-z]", password) and
# #             re.search(r"\d", password) and
# #             re.search(r"[!@#\$%\^&\*\(\)_\+]", password))

# # # 📝 Signup function
# # def signup():
# #     print("\n🔐 Signup")
# #     email = input("Enter email: ").strip()
# #     if not is_valid_email(email):
# #         print("❌ Invalid email format.")
# #         return
# #     if email in users:
# #         print("⚠️ Email already registered.")
# #         return

# #     password = getpass.getpass("Enter password (hidden): ")
# #     if not is_strong_password(password):
# #         print("❌ Weak password. Use 8+ chars with uppercase, lowercase, digit & symbol.")
# #         return

# #     users[email] = password
# #     print("✅ Signup successful!")

# # # 🔓 Login function
# # def login():
# #     print("\n🔓 Login")
# #     email = input("Enter email: ").strip()
# #     password = getpass.getpass("Enter password (hidden): ")

# #     if users.get(email) == password:
# #         print("✅ Logged in successfully!")
# #     else:
# #         print("❌ Invalid email or password.")

# # # 🚀 Main loop
# # def main():
# #     print("Welcome to the Secure Login System")
# #     while True:
# #         choice = input("\nChoose an action (signup / login / quit): ").lower()
# #         if choice == "signup":
# #             signup()
# #         elif choice == "login":
# #             login()
# #         elif choice == "quit":
# #             print("👋 Exiting program. Stay safe!")
# #             break
# #         else:
# #             print("Unknown option. Try again.")

# # # ▶️ Run the main loop
# # if __name__ == "__main__":
# #     main()

# def func1():


    
#     def func():

      
#         global x
#         x=10
#         print(x)
#     func()   
#     print(x)    

# func1()



set1={({1:"name",2:"age"})}
print(set1)