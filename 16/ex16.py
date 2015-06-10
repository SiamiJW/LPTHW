"""
EX 16: Reading and Writing Files 
Building a simple little text editor
"""

from sys import argv

script, filename = argv 

print "WE're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, "w") #not sure what the second parameter does

print "Truncating the file. Goodbye!"
target.truncate()


