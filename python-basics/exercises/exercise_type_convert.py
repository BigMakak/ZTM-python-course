import datetime

# Exercise for input and type conversions
birth_year = int(input("What was the year that you were born? \n"))
# Use the current date, that returns an int value
curr_year = datetime.date.today().year

print(f"You are {str(curr_year - birth_year)} years old!")

