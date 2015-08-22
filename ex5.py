my_name = 'Saurabh Kulshreshtha'
my_age = 23 # not a lie
my_height = 71 # inches
my_weight = 72 # kgs
my_eyes = 'black'
my_teeth = 'off-white'
my_hair = 'black'

print "Let's talk about %s.", % my_name
print "He's %d years old.", % my_age
print "He's %d inches tall.", % my_height
print "He's %d kilos heavy.", % my_weight
print "Actually it is quite heavy."
print "He's got %s eyes and %s hair.", % (my_eyes, my_hair)

# this line is tricky, try getting it exactly right
print "If I add %d, %d and %d then I get %d", % (my_age, my_height, my_weight, my_age + my_height + my_weight) 
