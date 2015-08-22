name = 'Saurabh Kulshreshtha'
age = 23 # not a lie
height = 71 # inches
weight = 72 # kgs
eyes = 'black'
teeth = 'off-white'
hair = 'black'

print "Let's talk about %s." % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d kilos heavy." % weight
print "Actually it is quite heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)

# this line is tricky, try getting it exactly right
print "If I add %d, %d and %d then I get %d" % (age, height, weight, age + height + weight) 
