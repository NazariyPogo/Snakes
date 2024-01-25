#The purpose of this program is to retrieve user input and display a message depending on whether the input is even or odd

num = False

while True:
    num = input("Welcome! Please enter a number of your choice to test for evenness or oddness: ")
    if(num.isdigit()):
        num = int(num)
        break
    print("You did not enter a valid number, please try again!")

check = False

while True:
    check = input("Please enter a second number by which to divide the first number: ")
    if(check.isdigit()):
        check = int(check)
        break
    print("You did not enter a valid number, please try again!")

result = num / check

if result % 1 == 0:
    if num % 4 == 0:
        print("The number " + str(num) + " is divisible by " + str(check) + " AND divisible by 4!")
    else:
        print("The number " + str(num) + " is divisble by " + str(check) + "!")
else:
    print("The number " + str(num) + " is NOT divisible by " + str(check) + "!")
