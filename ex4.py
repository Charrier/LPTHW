##Variable definition
#Define the amount of cars
cars = 100
#Define the amount seat in each car
space_in_a_car = 4
#Define the number of drivers
drivers = 30
#Define the number of passengers
passengers = 90
#Define the amount of cars that can't be driven
cars_not_driven = cars - drivers
#Define the amount of cars that can be driven
cars_driven = drivers
#Define the amount of passengers that can embark in a driven car
carpool_capacity = cars_driven * space_in_a_car
#Define the average number of passengers in each driven car
average_passengers_per_car = passengers / cars_driven

#Printable section
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."