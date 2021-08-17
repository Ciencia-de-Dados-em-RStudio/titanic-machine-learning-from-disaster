#Exercise: Lists
#Things get more interesting with lists.
#You'll apply your new knowledge to solve the questions below. Remember to run the following cell first.

from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *
print('Setup complete.')

#1.Complete the function below according to its docstring.
def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) >= 2: 
        return L[1]
    return None

# Check your answer
#q1.check()
L = [0]
select_second(L)
len(L)
#1

#Solution:
#Hint: Python starts counting at 0. So the second item isn't indexed with a 2
def select_second(L):
    if len(L) < 2:
        return None
    return L[1]
select_second(L)  
  
#2.You are analyzing sports teams. Members of each team are stored in a list.
#The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that.
#These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.
#Complete the function below to select the captain of the worst team.

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

# Check your answer
#q2.check()

#Solution:
#Hint: The last item in a list L can be selected with L[-1]. The first item in the first sublist would be selected as L[0][0]

def losing_team_captain(teams):
    return teams[-1][1]

#3.The next iteration of Mario Kart will feature an extra-infuriating new item, the Purple Shell.
#When used, it warps the last place racer into first place and the first place racer into last place. 
#Complete the function below to implement the Purple Shell's effect.

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[-1], racers[0] = racers[0],racers[-1]
    return
#Testing
racers = ["Mario", "Bowser", "Luigi"]
purple_shell(racers)
racers
#['Luigi', 'Bowser', 'Mario'] ok !
#Outro testing...
racers[-1], racers[2] = racers[2],racers[-1]
racers

#Solution:
#Hint: Your function should change the list it receives, but not return anything
#To swap the list elements, think back to the code you used in the very first exercise to swap two variables.
def purple_shell(racers):
    # One slick way to do the swap is x[0], x[-1] = x[-1], x[0].
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
purple_shell(racers)
racers   

#4.¶What are the lengths of the following lists? 
#Fill in the variable lengths with your predictions. 
#(Try to make a prediction for each list without just calling len() on it.)

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
​
# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]

# Check your answer
#q4.check()

#Correct:
#a: There are three items in this list. Nothing tricky yet.
#b: The list [2, 3] counts as a single item. It has one item before it. So we have 2 items in the list
#c: The empty list has 0 items
#d: The expression is the same as the list [2, 3], which has length 2.

#5. 🌶️
#We're using lists to record people who attended our party and what order they arrived in.
#For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
#A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. 
#However, they must not be the very last guest (that's taking it too far). 
#In the above example, Mona and Gilbert are the only guests who were fashionably late.
#Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    y = len(arrivals) - 1
    x = arrivals.index(name)
    return x != y and x >= len(arrivals)/2
      
# Check your answer
q5.check()

fashionably_late(party_attendees, "Mona") 


##Solution:
#Hint: Use the index method to find when the person arrived. Check whether that is a fashionably late spot given the list length (len). Think about 0-indexing

def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

fashionably_late(party_attendees, "Mona") 










    













