numbers=[]
while True:
    user_input = input("enter a number:")
    if user_input == "":
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)
print("five greatest numbers: ", numbers[:5])



