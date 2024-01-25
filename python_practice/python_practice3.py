#The purpose of this program is to retrieve either a hardcoded list or a list from user input and return all numbers less than 5

list = []
max_number_included = 4

while True:
    decision = input("Enter a 0 for a premade list or a 1 for a custom list: ")
    if decision.isdigit():
        decision = int(decision)
        break
    else:
        print("That is an invalid input, please enter a whole number!")

if decision is 1:
    list_size = None
    while True:
        list_size = input("Please enter the amount of numbers you want in the list: ")
        if list_size.isdigit():
            list_size = int(list_size)
            break
        else:
            print("That is an invalid input, please enter a whole number!")

    while True:
        max_number_included = input("Please enter the number you want as the maximum number in the result list: ")
        if max_number_included.isdigit():
            max_number_included = int(max_number_included)
            break
        else:
            print("That is an invalid input, please enter a whole number!")

    i = 0

    print("Please enter a number you want in the list: ")
    for i in range(list_size):
        while True:
            list_candidate = input()
            if list_candidate.isdigit():
                list.append(int(list_candidate))
                break
            else:
                print("That is an invalid input, please enter a whole number!")
else:
    list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

result_list = []

for num in list:
    if num <= max_number_included:
        result_list.append(num)

print("Out of the numbers you entered, the ones less than " + max_number_included + " are: " + result_list)
