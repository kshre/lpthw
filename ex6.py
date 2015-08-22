# format string ; joke set-up
x = "There are %d types of people." % 10
# string binary ; punchline element
binary = "binary"
# string do_not ; punchline element
do_not = "don't"
# format string ; Punchline
y = "Those who know %s and those who %s." % (binary, do_not)

# print the joke setup
print x
# print the joke punchline
print y

# repeat the joke setup; more format chars then arguments provided
print "I said: %r %d." % x
# repeat the joke punchline
print "I also said: '%s'." % y

# boolean ; joke evaluation
hilarious = False
# format string ; joke evaluation query and embedded variable response
joke_evaluation = "Isn't that joke so funny?! %r"

# print evaluation format with evaluation result
print joke_evaluation % hilarious

# string variable w
w = "This is the left side of..."
# string variable e
e = "a string with a right side."

# print concatenation of strings
print w + e
