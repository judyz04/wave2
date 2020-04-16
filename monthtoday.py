month = str(input("Enter the month name: "))
d30 = {"April", "June", "September", "November"} 
d32 = {"Feburary"}
if month in d30:
    print("There are 30 days.")
elif month in d32:
    print("There are 28 or 29 days.")
else:
    print("There are 31 days.")