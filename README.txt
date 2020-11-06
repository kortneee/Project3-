How to run template.py: 

The first step to running this program is opening the Windows Powershell application which
allows the user to view every file on the computer.

In order to access and use the template.py file, the command [python] must first be entered to interact
with any python sourced file. 

To run the program, template.py, the command [template.py] must be entered. If [template.py] is entered plainly,
an output message will be recieved by the user with information on how to correctly enter variable, text,
and output files. To run the program, three commands must be entered directly after the [template.py] command.

The command that directly follows [template.py] shoud be a call to a variable file that already exists. 
The file should contain a variable or multiple variables, each corresponding with a value. For example if the user
were to call the vars.txt file, the user must enter the command [vars.txt].

Following the variable file command, a command to a text file containing paragraphs, lists, or hashtags
must be given. As with vars.txt, to call the in.txt file, the command [in.txt] must be made.

The final command given will call an output html file, and can be named anything as long as it 
is followed by [.html]. This file will be edited in the template.py code to create an html file 
and automatically be placed in the users directory. For example if the user wanted to create an html
file called 'out' the command that must be entered is [out.html]

Once a command such as [template.py vars.txt in.txt out.html] is made, the user will be able to access this
out.html file in the File Explorer application, as well as the Windows Powershell application. 

What is contained in the 'out.html' file, is a version of 'in.txt'. The html version is formatted so it can be opened
as a html in Chrome, Firefox, or Safari. The html version also replaces each line containing a # as blank, and each 
@ as a list with bulletpoints. Each instance of word with a '$' in front and end of it will be replaced by the
corresponding value found in the variable textfile. For example if the input text file contains the line
"This project is $almost$ finished", and the variable textfile contains, "$almost$ = never", the resulting
line in the html file should be "This project is never finished".

To open this file in Chrome/Firefox/Safari the user must navigate to the File Explorer application
where they can click on the file, for this example the file would be named 'out'. 