name = 'Saurabh Kulshreshtha'
age = 23 # not a lie
height = 71 # inches
weight = 72 # kgs
eyes = 'black'
teeth = 'off-white'
hair = 'black'

# conversions
one_inch_to_cm = 2.54
one_kilo_to_pound = 2.20
weight_pounds = weight * one_kilo_to_pound
height_cms = height * one_inch_to_cm
print "Weight:", weight_pounds, "lbs, Height:", height_cms, "centimeters."
print

# print to terminal
print "Let's talk about %s." % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d kilos heavy." % weight
print "Actually it is quite heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)

# this line is tricky, try getting it exactly right
print "If I add %d, %d and %d then I get %d" % (age, height, weight, age + height + weight) 
