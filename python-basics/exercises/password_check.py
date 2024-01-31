user_name = str(input("What\'s is your name? \n"))

password = str(input("Write your password: "))

password_size = len(password)

counter = password.replace("%a","*")

print(counter)

print(f"Hello {user_name}, your password: {'*' * password_size} is {str(password_size)} letters long")