import random
dice=int(input ("How many dice to roll?"))
total_sum=0
for i in range(dice):
    number =random.randint(1,6)
    print(number)
    total_sum+=number
print(f"the sum of the {dice} dice rolled is: {total_sum}")