from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third	


# Réinstancier les valeurs à partir d'un prompt utilisateur

first = raw_input("What's the first value?")
second = raw_input("What's the second value?")
third = raw_input("What's the thir value?")

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third	

