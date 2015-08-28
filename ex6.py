x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Many format characters can be used in a row if added between (x, y)
y = "Those who know %s and those who %s." % (binary, do_not)

#Display the content of the variable defined earlier 
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Display the content of variable "joke_evaluation" which has a format character (%r : for raw data) calling the content of the "hilarious" variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#concatenate strings w and e
print w + e