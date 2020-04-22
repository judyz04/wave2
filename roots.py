a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))
c = int(input("Enter the c value: "))

# calculate the discriminant
d = (b**2) - (4*a*c)

if d > 0:
    print("There are no roots.")
elif d == 0:
    print("There is 1 root.")
else:
    result1 = (-b - d)/(2*a)
    result2 = (-b + d)/(2*a)
    print("There is more than 2 roots. The values are " + str(result1) + " and " + str(result2) + ".")
