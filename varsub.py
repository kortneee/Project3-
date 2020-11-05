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
    for w in words:
        if w[0] == "$" and w[:-1] == "$":
            for key, value in vars.items():
                if key == w:
                    print (value) 
                if key == w[1:-1]:
                    print(value)