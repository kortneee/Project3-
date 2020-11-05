""""Replaces references to variables associated with them"""
# MSC 260 Fall 2020 Project 3
# Kortnee Reiss
# Decleration: I, Kortnee Reiss, am the sole author of this code, which was developed in 
#   accordance with the rules in the course syllabus.
import os
def substitute(vars,s):
    """Takes dictionary vars, and replaces the string, s, with the variables's matching value
    in vars"""
    varin= open(vars,"r")
    dictvals = dict(x.split("=") for x in varin.split())
    for key, value in dictvals.items():
        if key == s: 
            return value