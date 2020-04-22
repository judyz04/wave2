while True:  
  oddSet = ['a', 'c', 'e', 'g']
  evenSet = ['b', 'd', 'f', 'h']
  oddNumbers = [1, 3, 5, 7]
  evenNumbers = [2, 4, 6, 8]
  l = input("Enter the letter: ")
  number = int(input("Enter the number: "))
  if l.lower() in oddSet and number in oddNumbers:
    print("The square is black.")
  elif l.lower() in evenSet and number in oddNumbers:
    print("The square is white.")
  elif l.lower() in evenSet and number in evenNumbers:
    print("The square is black.")
  else:
    print("The square is white.")