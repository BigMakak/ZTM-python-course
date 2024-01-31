# PYTHON BASICS Notes

name = 3
print( 3 // 4) #Clean division
print( 3 ** 2) #Power operator
print("My variable is of type" + str(type(name)))

#Math functions
print(round(3.6)) #Rounding numbers
print(abs(-10)) #Absolute numbers

#Bin and complex 

print("BIN AND COMPLEX")
print(bin(4))
print(int("0b100",2)) # Convert this binary representation of base 2(binary) into a integer

#Variables
print("VARIABLES")
a,b,c = 1,2,3 #Multiple assign is possible

print(1 + 2 + 3)

#Augment assign operator

value_var = 4
value_var += + 1
value_var -= 2
print("Value of plus var: " + str(value_var))

#strings
print("STRINGS")

# Long string can be made with 3 ->""" or 3 -> '''
long_string = """ 
Woow baby
/// --- ///
-.-
"""
print(long_string)

# String concatenation an type conversion
print("Hello baby " + "what type is this: " + str(type(str(100))))

# Formated string and escaping 

user_name = "Jorge Manuel"
age = 56

print(f"Hello {user_name}, you are {age} years hold")
print("Hello baby, {} this is my favourite food: {food}".format(user_name,food="Burguer"))

#string indexes
print("## STRING INDEXES ##")
actor = "Jonny Travolta" # Access specific indexes on the string, like a list or array

print(actor[7])

#[start:stop:stepover]
# start -> The start index to look for
# stop ->  were we stop looking in the array
# stepover -> How many steps we are taking in the iteration

print(actor[0:7:2])
print(actor[::2]) # When we don't specify something, it will use a default value(start at 0, stop at the end of the list/string)
print(actor[:5:1])
print(actor[2::-1]) # iterate starting at the end, using the minus operator

# Methods and Built in functions
print("BUILT IN FUNCTIONS/FUNCTIONS")
quote = "to be or not to be"

print(quote.find("not")) # Internal Methods of strings, as there are many other methods for other data types

quote2 = quote.replace("to","suck") # The first string is immutable, so to change it permantly we need to create/or arrange a new variable

print(quote2)
print(quote)


