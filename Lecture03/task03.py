smallest =int(input("enter number:"))
largest = smallest
while True:
    number= input("enter number:")
    if number == "":
        break
    number=int(number)

    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

    print("smallest : ",smallest)
    print("largest : ",largest)
