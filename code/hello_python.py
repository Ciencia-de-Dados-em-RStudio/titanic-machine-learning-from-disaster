spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

#
type(spam_amount)
#It's an int - short for integer. There's another sort of number we commonly encounter in Python:
type(19.95)
#A float is a number with a decimal place - very useful for representing things like weights or proportions.

#type() is the second built-in function we've seen (after print()), and it's another good one to remember. 
#It's very useful to be able to ask Python "what kind of thing is this?".
type (viking_song)
type (print)

#"True division" is basically what your calculator does:
print(5 / 2)
print(6 / 2)
#It always gives us a float.

#The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)
print(6 // 2)

#Order of operations
#The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. 
#Some remember these by a mnemonic such as PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
#Python follows similar rules about which calculations to perform first. They're mostly pretty intuitive.

#Sometimes the default order of operations isn't what we want:
hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
#Parentheses are useful here. 
#You can add them to force Python to evaluate sub-expressions in whatever order you want.
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

#Builtin functions for working with numbers
#min and max return the minimum and maximum of their arguments, respectively...
print(min(1, 2, 3))
print(max(1, 2, 3))

#abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))

#In addition to being the names of Python's two main numerical types, int and float can also be called 
#as functions which convert their arguments to the corresponding type:

print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
