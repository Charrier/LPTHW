name = 'PH C'
age = 26 # not a lie
height_cm = 187 # cm
height_in = round(height_cm / 2.54) # inches
weight_kg = 68.7 #cm
weight_lb = round(weight_kg * 1.45359237) # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r cm tall." % height_cm
print "He's %r inch tall." % height_in
print "He's %r kg heavy." % weight_kg
print "He's %r lb heavy." % weight_lb
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)