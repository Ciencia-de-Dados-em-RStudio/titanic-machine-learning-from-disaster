
#This notebook is an exercise in the Python course. You can reference the tutorial at this link.

#Welcome to your first set of Python coding problems. If this is your first time using Kaggle Notebooks, welcome!

#Notebooks are composed of blocks (called "cells") of text and code. Each of these is editable, though you'll mainly be editing the code cells to answer some questions.

#To get started, try running the code cell below (by pressing the ► button, or clicking on the cell and pressing ctrl+enter on your keyboard).

#line inserted above
print("You've successfully run some Python code")
print("Congratulations!")

viking_song = "Spam " * 4
print(viking_song)

#line inserted bellow
#Try adding another line of code in the cell above and re-running it.

#Now let's get a little fancier: Add a new code cell by clicking on an existing code cell, hitting the escape key, and then hitting the a or b key. The a key will add a cell above the current cell, and b adds a cell below.

#Great! Now you know how to use Notebooks.

#Each hands-on exercise starts by setting up our feedback and code checking mechanism. Run the code cell below to do that. Then you'll be ready to move on to question 0.

#0.
#This is a silly question intended as an introduction to the format we use for hands-on exercises throughout all Kaggle courses.

#What is your favorite color?

#To complete this question, create a variable called color in the cell below with an appropriate value. The function call q0.check() (which we've already provided in the cell below) will check your answer.

# create a variable called color with an appropriate value on the line below
# (Remember, strings in Python must be enclosed in 'single' or "double" quotes)
#____
color = "blue"
# Check your answer
#q0.check()
#Correct: What?! You got it right without needing a hint or anything? Drats. Well hey, you should still continue to the next step to get some practice asking for a hint and checking solutions. (Even though you obviously don't need any help here.)
#Delete the # in the line below to make one of the lines run. You can choose between getting a hint or the full answer by choosing which line to remove the # from.

#Removing the # is called uncommenting, because it changes that line from a "comment" which Python doesn't run to code, which Python does run.

#q0.hint()
#q0.solution()
#Solution:

#color = "blue"
#The upcoming questions work the same way. The only thing that will change are the question numbers. For the next question, you'll call q1.check(), q1.hint(), q1.solution(), for question 2, you'll call q2.check(), and so on.

#1.
#Complete the code below. In case it's helpful, here is the table of available arithmetic operations:

#Operator	Name	          Description
#a + b	  Addition	      Sum of a and b
#a - b	  Subtraction	    Difference of a and b
#a * b	  Multiplication  Product of a and b
#a / b	  True division	  Quotient of a and b
#a // b	  Floor division  Quotient of a and b, removing fractional parts
#a % b	  Modulus	Integer remainder after division of a by b
#a ** b	  Exponentiation	a raised to the power of b
#-a	      Negation	      The negative of a

pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
#____
radius = diameter / 2
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
#____
area = pi * radius ** 2
# Check your answer
#q1.check()
#Correct

# Uncomment and run the lines below if you need help.
#q1.hint()
#q1.solution()
#Hint: The syntax to raise a to the b'th power is a ** b

#Solution:

radius = diameter / 2
area = pi * radius ** 2
#2.
#Add code to the following cell to swap variables a and b (so that a refers to the object previously referred to by b and vice versa).

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
#q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.
#tmp = a
#a = b
#b = tmp
a, b = b, a
######################################################################

# Check your answer
#q2.check()
#Correct:

#The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:

tmp = a
a = b
b = tmp

#If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:

a, b = b, a

#We'll demystify this bit of Python magic later when we talk about tuples.

#q2.hint()
#Hint: Try using a third variable.

#q2.solution()
#Solution: The most straightforward solution is to use a third variable to temporarily store one of the old values. e.g.:

tmp = a
a = b
b = tmp

#If you've read lots of Python code, you might have seen the following trick to swap two variables in one line:

a, b = b, a

#We'll demystify this bit of Python magic later when we talk about tuples.

#3a.
#Add parentheses to the following expression so that it evaluates to 1.

(5 - 3) // 2
#1
#q3.a.hint()
#Hint: Following its default "BEDMAS"-like rules for order of operations, Python will first divide 3 by 2, then subtract the result from 5. You need to add parentheses to force it to perform the subtraction first.

# Check your answer (Run this code cell to receive credit!)
#q3.a.solution()
#Solution:

(5 - 3) // 2
#3b. 🌶️
#Questions, like this one, marked a spicy pepper are a bit harder.

#Add parentheses to the following expression so that it evaluates to 0.

(8 - 3) * (2 - (1 + 1))
#0
#q3.b.hint()
# Check your answer (Run this code cell to receive credit!)
#q3.b.solution()
#Solution: 
(8 - 3) * (2 - (1 + 1)) #is one solution. There may be others.

#4.
#Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.

#Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
alice_candies + bob_candies + carol_candies

to_smash = (alice_candies + bob_candies + carol_candies) % 3 

# Check your answer
#q4.check()
#Correct

##q4.hint()
#q4.hint(2)
#q4.solution()
#Hint 1: You'll probably want to use the modulo operator, %. (For another hint, call .hint(2))

#Hint 2: j % k is the remainder after dividing j by k

#Keep Going
#Next up, you'll learn to write new functions and understand functions others write. This will make you at least 10 times more productive as a Python programmer.

