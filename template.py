"""Format a textfile to HTML supporting bullet lists, comments, and variable replacement
"""
# MSC 260 Fall 2020 Project 3
# Kortnee Reiss
# Decleration: I, Kortnee Reiss, am the sole author of this code, which was developed in 
#   accordance with the rules in the course syllabus.
import sys
import os
import varsub
if len(sys.argv) != 3: 
    print("Usage: {} INFILE OUTFILE".format(sys.argv[0]))
    print("The text file INFILE is then converted to an HTML file OUTFILE.")
    sys.exit()

# take input and output files
varsfn = sys.argv[1]    #variable filename
infn = sys.argv[2]      #input text filename
outfn = sys.argv[3]     #output HTML filename

# open input and output files
fin = open(infn,"r")
fout = open(outfn,"w")

# print header
fout.write("<!DOCTYPE html>\n")
fout.write("<html>\n")
fout.write("<head><title>HTML document</title></head>\n")
fout.write("<body>\n")
opentags = []  # Stack containing open tags inside <body>
               # (only a single p tag, in this program)
for line in fin:
    isblank = not bool(line.strip())
    if opentags and isblank:
        checkwords = opentags[0]
        words = checkwords.split()
        word = 0
        #Checks each word in opentags for $, #, and @, and edits the string accordingly 
        for word in len(words):
            currword = words[word] 
            if currword[0] == "$" and currword[:-1] == "$":
                word = varsub.substitute(varsfn,currword[1:-1])
            if currword[0] == '#':
                opentags.remove()
            elif currword[0] == '@':
                fout.write("<ul>\n")
                fout.write("<li>",checkwords)
                fout.write("</li>\n")
                fout.write("</ul>\n")
                opentags.remove()
        if len(opentags) == 0:
            continue
        else: 
            fout.write("</{}>\n".format(opentags.pop()))
    if not isblank:
        # Line is not blank, must appear in output
        if not opentags:
            # No tags open; start a new paragraph
            fout.write("<p>\n")
            opentags.append("p")
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
