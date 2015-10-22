from sys import argv

script, filename = argv

print "We're going to erase %r" %script
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

raw_input("?")

print "Open the file ..."
target = open(filename, "w")

#Les droits en ecriture doivent etre octroyes pour la fonction "tronquer" (supprimer)
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

print "Still, let see what you have written"
target = open(filename)
print target.read()

print "What's the first line again?"
print target.readline()
