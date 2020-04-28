from random import randrange
#spin wheel :D
value = randrange(0,38)

if value == 37:
    print("The spin resulted in 00.")
else: 
    print("The spin resulted in %d." % value)

#single numbers
if value == 37:
    print("Pay 00")
else:
    print("Pay", value)

#conditioning for colours 
if value % 2 == 1 and value >= 1 and value <= 9 or \
    value % 1 == 0 and value >= 12 and value <= 18 or \
    value % 2 == 1 and value >= 19 and value <= 27 or \
    value % 2 == 0 and value >= 30 and value <= 36:
   print("Pay Red")
elif value == 0 or value == 37:
    pass
else:
    print("Pay Black.")

#odd or even
if value >= 1 and value <= 36:
    if value % 2 == 1:
        print("Pay odd.")
    else:
        print("Pay even.")

#lower vs higher number 

if value >= 1 and value <= 18:
    print("Pay 1 to 18")
elif value >= 19 and value <= 36:
    print("Pay 19 to 36")