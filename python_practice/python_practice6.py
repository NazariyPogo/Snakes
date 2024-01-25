#The purpose of this program is to identify palindromes from user input.

def compare_to_reverse_string(text):
    for i in range(len(text)):
        if text[i] is not text[len(text) - (i + 1)]:
            return False
    return True

def get_user_input():
    while True:
        decision = input("Enter a string: ")
        if decision.isalpha():
            return str(decision)
        else:
            print("That is an invalid input!")

test_string = get_user_input()

if compare_to_reverse_string(test_string):
    print("'{test_string}' is a palindrome!")
else:
    print("'" + test_string + "' is NOT a palindrome!")

#Alternate solution - have the word reversed in a separate method and compare it to the original word (my idea is better)
    
def reverse(text):
    res = ''
    for i in range(len(text)):
        res += text[len(text) - 1 - i]
    return res

if test_string == reverse(test_string):
    print("'" + test_string + "' is a palindrome!")
else:
    print("'" + test_string + "' is NOT a palindrome!")