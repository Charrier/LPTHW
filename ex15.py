#indicates that the script will load the parameters from initial command line
from sys import argv

#defines the arguments in the commande line (script name then the filename to be run)
script, filename = argv

#defines a txt variable that opens the file to be run 
txt = open(filename)

#print the following sentence followed by the content of the file 
print "Here's your file %r:" % filename
print txt.read()

#define the filename from a user prompt
print "Type the filename again:"
file_again = raw_input("> ")

#defines a txt_again variable that opens the file to be run 
txt_again = open(file_again)

#print the content of the file 
print txt_again.read()

#essai de la comande close()
txt_again = close(file_again)
print txt_again.read()
