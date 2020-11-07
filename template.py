"""Format a textfile to HTML supporting bullet lists, comments, and variable replacement
"""
# MSC 260 Fall 2020 Project 3
# Kortnee Reiss
# Decleration: I, Kortnee Reiss, am the sole author of this code, which was developed in 
#   accordance with the rules in the course syllabus.
import sys
import os
import varsub
# take input and output files 
try: 
    varsfn = sys.argv[1]    #variable filename
    infn = sys.argv[2]      #input text filename
    outfn = sys.argv[3]     #output HTML filename
except IndexError: 
    print("template.py requires three command line arguments")
    print("Usage: python template.py variable.txt infile.txt outfile.html")
    sys.exit()

try:
    fin = open(infn,"r")
except OSError: 
    ("Input file does not exist")
try: 
    varin = open(varsfn, "r")
except OSError: 
    ("Variable file does not exist")
try:
    fout = open(outfn,"w")
except OSError: 
    ("Output file cannot be opened")

# Print header
fout.write("<!DOCTYPE html>\n")
fout.write("<html>\n")
fout.write("<head><title>HTML document</title></head>\n")
fout.write("<body>\n")
opentags = []       # Stack containing open tags inside <body>
whitespace = False  # Keep track of whitespaces
for line in fin:
    isblank = not bool(line.strip())
    if opentags and isblank:
        fout.write("</{}>\n".format(opentags.pop()))
    if not isblank:
        ls = line.strip().split(" ")
        whitespace =True

        #Ends processing line if begins with #
        if ls[0] == '#':  
            continue

        #Adds list to out file if line begins with @
        if ls[0] == '@':
            if not opentags:
                fout.write("<ul>\n")
                opentags.append("ul")
            line = line[1:]
            fout.write("<li>\n")
            fout.write(line)
            fout.write("</li>\n")
            continue   #Ends processing list

        #writes paragraph if no tags open
        if not opentags:
            fout.write("<p>\n")
            opentags.append("p")
        
        #enters varsub as a dict to substitute words
        varsdict = {}
        for f in varin:
            (key, val) = f.split("=")
            varsdict[key] = val.strip("\n")
        line = varsub.substitute(varsdict,line)

        #Adds space to paragraph so end word of lineA and start word 
        #line B dont combine
        if whitespace:
            fout.write(" ")
        fout.write(line)
fin.close()

# close all open tags in the body
while opentags:
    fout.write("</{}>\n".format(opentags.pop()))

# print the standard footer that closes body and html tags
fout.write("</body>\n")
fout.write("</html>\n")

# done writing to output file
fout.close()