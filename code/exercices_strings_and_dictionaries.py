

#You are almost done with the course. Nice job!
#We have a couple more interesting problems for you before you go.
#As always, run the setup code below before working on the questions.

#from learntools.core import binder; binder.bind(globals())
#from learntools.python.ex6 import *
print('Setup complete.')
#
#Let's start with a string lightning round to warm up. What are the lengths of the strings below?
#For each of the five strings below, predict what len() would return when passed that string. 
#Use the variable length to record your answer, then run the cell to check whether you were right.

#0a.
a = ""
length = 0
#q0.a.check()
#Correct:
#The empty string has length zero. 
#Note that the empty string is also the only string that Python considers as False when converting to boolean.

#0b.¶
b = "it's ok"
length = 7
#q0.b.check()
#Correct:
#Keep in mind Python includes spaces (and punctuation) when counting string length.

#0c.
c = 'it\'s ok'
length = 7
#q0.c.check()
#Correct:
#Even though we use different syntax to create it, the string c is identical to b. 
#In particular, note that the backslash is not part of the string, so it doesn't contribute to its length

#0d.¶
d = """hey"""
length = 3
q0.d.check()
#Correct:
#The fact that this string was created using triple-quote syntax doesn't make any difference in terms of its content or length. 
#This string is exactly the same as 'hey'.

#0e.
e = '\n'
length = 1
#q0.e.check()
#Correct:
#The newline character is just a single character! 
#(Even though we represent it to Python using a combination of two characters.)

# 1.There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." 
#Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. 
#For our purposes, a valid zip code is any string consisting of exactly 5 digits.
#HINT: `str` has a method that will be useful here. Use `help(str)` to review a list of string methods.
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """ 
    if len(zip_code) == 5 and str.isdigit(zip_code):
            return True
    else:
            return False

# Check your answer
#q1.check()
is_valid_zip('1122')
#False
is_valid_zip('')
#False
is_valid_zip('19125')
#True

#Solution:
def is_valid_zip(zip_str):
    return len(zip_str) == 5 and zip_str.isdigit()
is_valid_zip('')
#False

## 2.A researcher has gathered thousands of news articles. 
#But she wants to focus her attention on articles including a specific word. 
#Complete the function below to help her filter her list of articles.
#Your function should meet the following criteria:
#- Do not include documents where the keyword string shows up only as a part of a larger word. 
#  For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.” 
#- She does not want you to distinguish upper case from lower case letters. 
#  So the phrase “Closed the case.” would be included when the keyword is “closed”
#- Do not let periods or commas affect what is matched. 
#  “It is closed.” would be included when the keyword is “closed”. 
#  But you can assume there are no other types of punctuation.

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    pass

# Check your answer
#q2.check()
#Hint: Some methods that may be useful here: str.split(), str.strip(), str.lower().
#Solution
def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword = "casino"
word_search(doc_list, keyword)
#[0]
keyword="car"
word_search(doc_list, keyword)
#[1]

## 3.Now the researcher wants to supply multiple keywords to search for. 
#Complete the function below to help her.
#(You're encouraged to use the `word_search` function you just wrote when implementing this function. 
#Reusing code in this way makes your programs more robust and readable - and it saves typing!)
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(doc_list, keyword)
    return keyword_to_indices

# Check your answer
#q3.check()
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
multi_word_search(doc_list, keywords)
#{'casino': [0, 1], 'they': [1]}


