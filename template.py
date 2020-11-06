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

# open input and output files
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

# print header
fout.write("<!DOCTYPE html>\n")
fout.write("<html>\n")
fout.write("<head><title>HTML document</title></head>\n")
fout.write("<body>\n")
opentags = []  # Stack containing open tags inside <body>
whitespace = False
for line in fin:
    isblank = not bool(line.strip())
    if opentags and isblank:
        fout.write("</{}>\n".format(opentags.pop()))
    if not isblank:
        ls = line.strip().split(" ")
        if ls[0] == '#':
            whitspace = True
            continue
        # Line is not blank must appear in output
        if not opentags:
            # No tags open; start a new paragraph
            fout.write("<p>\n")
            opentags.append("p")
        line = varsub.substitute(varsfn,line)
        if ls[0] == '@':
            line = line[1:]
            fout.write("<ul>\n")
            fout.write("<li>\n")
            fout.write(line)
            fout.write("</li>\n")
            fout.write("</ul>\n")
        if whitespace: 
            fout.write(" ")
        fout.write(line)
# done reading from input file
fin.close()
# close all open tags in the body
while opentags:
    fout.write("</{}>\n".format(opentags.pop()))
# print the standard footer that closes body and html tags
fout.write("</body>\n")
fout.write("</html>\n")

# done writing to output file
fout.close()
print(fout)