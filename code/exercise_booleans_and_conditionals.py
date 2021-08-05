#exercice: Booleans and Conditionals

#1.
#Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own!
#In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
# Your code goes here. Define a function called 'sign'
def sign(x):
    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    else:
        return(0)
# Check your answer
#q1.check()
sign(0)
sign(-3)
sign(1)
#Solution:
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

#2.
#We've decided to add "logging" to our to_smash function from the previous exercise.      
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
#What happens if we call it with total_candies = 1?
to_smash(1)
     
#That isn't great grammar!
#Modify the definition in the cell below to correct the grammar of our print statement. 
#(If there's only one candy, we should use the singular "candy" instead of the plural "candies")      

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies > 1:
        no_candies = "candies"
    else:
        no_candies = "candy"
    print("Splitting", total_candies, no_candies)
    return total_candies % 3

to_smash(91)
to_smash(1)
#Solution: A straightforward (and totally fine) solution is to replace the original print call with:

if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
#Here's a slightly more succinct solution using a conditional expression:
print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = True
rain_level = 0.0
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)
# Check your answer
#q3.check()
#Incorrect

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 6.0
have_hood = False
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)
# Check your answer
#q3.check()
#Corect!!

#Correct:
#One example of a failing test case is:
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)
#Correct
#Clearly we're prepared for the weather in this case. It's not raining. Not only that, it's not a workday, so we don't even need to leave the house! But our function will return False on these inputs.
#The key problem is that Python implictly parenthesizes the last part as:
#(not (rain_level > 0)) and is_workday
#Whereas what we were trying to express would look more like:
#not (rain_level > 0 and is_workday)

#4.
#The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.
#However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.
#See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative. (HINT: you don't even need Python's ternary syntax)     
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return True if number < 0 else False # Your code goes here (try to keep it to one line!)

# Check your answer
#q4.check()
concise_is_negative(1)

#Solution:
def concise_is_negative(number): 
  return number < 0

concise_is_negative(1)
concise_is_negative(-1)

#5a.
#The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog.
#We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. 
#For example:
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion
  
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    #pass
    return ketchup and mustard and onion
  
# Check your answer
#q5.a.check()
#Hint: You'll need to use the and operator.
#Solution:
#return ketchup and mustard and onion
wants_all_toppings(0,1,1)

#5b.
#For the next function, fill in the body to match the English description in the docstring.
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

# Check your answer
#q5.b.check()
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)
wants_plain_hotdog(0,0,0)
wants_plain_hotdog(0,1,0)

#5c.
#You know what to do: for the next function, fill in the body to match the English description in the docstring.
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)

# Check your answer
#q5.c.check()


#6. 🌶️
#We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise. What happens if we call int() on a bool? Try it out in the notebook cell below.
#Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1
 

# Check your answer
#q6.check()
exactly_one_topping(0,0,0)

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup + mustard + onion) == 1
exactly_one_topping(1,1,1)
exactly_one_topping(1,0,0)

#7. 🌶️ (Optional)
#In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

#The player is dealt two face-up cards. The dealer is dealt one face-up card.
#The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
#The dealer then deals additional cards to himself until either:
#the sum of the dealer's cards exceeds 21, in which case the player wins the round
#the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
#When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)

#For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False
q7.simulate_one_game()


def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    return False

q7.simulate(n_games=50000)


