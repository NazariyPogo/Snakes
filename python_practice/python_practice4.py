#The purpose of this program is to list the divisors of a number provided by the user.

print("Welcome! Please enter a number to see a list of divisors: ")
while True:
    decision = input()
    if decision.isdigit():
        decision = int(decision)
        break
    else:
        print("That is an invalid input, please enter a whole number!")

range_of_nums = range(1, decision + 1)
list_of_divisors = []

for num in range_of_nums:
    if(decision % num == 0):
        list_of_divisors.append(num)

print("The divisors of " + str(decision) + " are: ")
print(list_of_divisors)