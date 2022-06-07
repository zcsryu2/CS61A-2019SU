""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    fl = open(path)
    lst = readlines(fl)
    for i in range(len(lst)):
        lst[i] = strip(lst[i])
    close(fl)
    return lst

def new_sample(path, i):
    line = lines_from_file(path)
    return line[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    lst = []

    words_num = len(typed_string) / 5
    v = words_num * 60 / (end_time - start_time)
    lst.append(v)

    lst0 = split(sample_paragraph)
    lst1 = split(typed_string)
    correct_num = 0
    if len(lst0) > len(lst1):
        length = len(lst1)
    else:
        length = len(lst0)
    for i in range(length):
        if lst0[i] == lst1[i]:
            correct_num += 1
    if length == 0:
        percent = 0.0
    else:
        percent = correct_num * 100 / length
    lst.append(percent)
    return lst

def pig_latin(words):
    i = 0
    for i in range(len(words)):
        if words[i] in "aoeiu":
            break
    if i == 0:
        return words + 'way'
    return words[i:] + words[:i] + 'ay'

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list, key = lambda x: score_function(user_input, x))

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
