#The purpose of this program is to state whether an input number is prime or not

from math import floor

print("Welcome! Please enter a number to see if it is prime: ")
while True:
    decision = input()
    if decision.isdigit():
        decision = int(decision)
        break
    else:
        print("That is an invalid input, please enter a whole number!")

range_of_nums = range(1, floor(decision / 2 + 1))
list_of_factors = []

for num in range_of_nums:
    if((decision / num) % 1 == 0):
        list_of_factors.append(num)
list_of_factors.append(decision)

if(len(list_of_factors) == 2):
    print(f"{decision} is a prime number")
else:
    print(f"{decision} is not a prime number, its factors are: ")
    print(list_of_factors)