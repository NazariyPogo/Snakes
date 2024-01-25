#The purpose of this program is to take a number from the user and present that many fibonnaci numbers

def get_user_input():
    while True:
        decision = input("Enter a number: ")
        if decision.isdigit():
            decision = int(decision)
            return decision
        else:
            print("That is an invalid input, please enter a whole number!")

#While loop solution
def get_fib_nums(amount):
    res = []
    prev_sum = 0
    prev_prev_sum = 0
    fib_num = 1
    while amount != 0:
        res.append(fib_num)
        prev_prev_sum = prev_sum
        prev_sum = fib_num
        fib_num = prev_sum + prev_prev_sum
        amount -= 1
    return res

#Recursive solution (limited to 990ish)
def recurse(num):
    res = []
    return recurse_list(res, 0, 0, 1, num)

def recurse_list(list, num1, num2, fib_num, count):
    if count > 0:
        count -= 1
        list.append(fib_num)
        num1 = num2
        num2 = fib_num
        fib_num = num1 + num2
        return recurse_list(list, num1, num2, fib_num, count)
    return list


num = get_user_input()
print(get_fib_nums(num))
print(recurse(num))