from sys import argv

#defining the arguments used as input from the command line  
script, input_file = argv

#defining the print_all function, with f pointing the a file variable that will be read
def print_all(f):
	print f.read()

#defining the rewind function: it points to the beginning of the file 
def rewind(f):
	f.seek(0)

#defining the print_a_line function, once called, it'll 
def print_a_line(line_count, f):
	print line_count, f.readline()

#opening the file in read mode
current_file = open(input_file)

print "First let's print the whole file:\n"

#printing the whole content of the file previously opened in read mode
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#setting the pointer to 0 in the current_file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)