#The purpose of this program is to generate a random password of varying strength by using either common words, only letters, or 72 character types

import random

def main(strength):
    pass_length = random.randint(8,15)
    easy_pass_words = ['password', 'myname', 'companyname', '12345', 'abcde']
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?'
    password = ''

    if strength.isdigit() and (strength == '1' or strength == '2' or strength == '3'):
        strength = int(strength)

        if strength == 1:
            for _ in range(3):
                password += random.choice(easy_pass_words)
        else:
            for x in range(pass_length):
                if strength == 2:
                    password += random.choice(valid_chars[0:52])
                elif strength == 3:
                    password += random.choice(valid_chars)

        return f"Your new password is: {password}"
    else:
        return "//The password strength entered is invalid//"

strength = input("Enter 1 for a weak password, 2 for a medium password, or 3 for a string password: ")
print(main(strength))