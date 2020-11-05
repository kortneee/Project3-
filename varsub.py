""""Module which replaces references to variables associated them, from a dictionary"""
# MSC 260 Fall 2020 Project 3
# Kortnee Reiss
# Decleration: I, Kortnee Reiss, am the sole author of this code, which was developed in 
#   accordance with the rules in the course syllabus.
import os
def substitute(vars,s):
    """Takes dictionary vars, and replaces the string, s, with the variables's matching value
    in vars"""
    words = s.split()
    index = 0
    #Returns index of variable to be swapped
    for i in range(len(words)):
        word= words[i]
        if word[0] == '$' and word[-1]=='$':
            index = i

    #checks dictionary keys for matches to variable, and swaps 
    # the variable with the cooresponding value in dictionary 
    for key, value in vars.items():
        check = str(key)
        if check[0]=='$' and check[-1]=='$':
            del words[index]
            words.insert(index,value)
        if check == (words[index])[1:-1]:
            del words[index]
            words.insert(index,value)
    output = ' '.join(words)
    return(output)