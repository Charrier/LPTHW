#defining the function, it's about printing two variables 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

#printing the function with the two variables straight with the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside to"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can conbine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Choose your own amount"
amount_of_cheese = int(raw_input("#Cheese: "))
amount_of_crackers = int(raw_input("#Crackers: "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)