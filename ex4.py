# cars available
cars = 100
# seating capacity of the cars
space_in_a_car = 4
# drivers available
drivers = 30
# passengers available
passengers = 90
# cars that won't be driven due to lack of drivers
cars_not_driven = cars - drivers
# cars driven
cars_driven = drivers
# max capacity of driven cars
carpool_capacity = cars_driven * space_in_a_car
# average number of people to be seated per car today 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
