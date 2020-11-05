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
    #checks each word in the string to see if its a variable
    for i in range(len(words)):
        word = words[i]
        if word[0] == '$' and word[-1]=='$':
            #if the word is a variable, the cooresponding key in the dictionary
            # replaces the variable in the list words
            for key, value in vars.items():
                check = str(key)
                if check[0]=='$' and check[-1]=='$':
                    del words[i]
                    words.insert(i,value)
                if check == (words[i])[1:-1]:
                    del words[i]
                    words.insert(i,value)
    #convert list to string
    output = ' '.join(words)
    return(output)