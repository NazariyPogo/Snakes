#The purporse of this program is to find the year that a person will turn 100.
#More work can be done in the form of input checking and better verifying whether the person had their birthday this year.

import datetime

print("Welcome to the 'Year at Age 100' Game!\n")
name = input("What is your name? ")
age = int(input("\nAnd how old will you be by the end of the year? "))

year_at_100 = str(datetime.date.today().year + (100-age))

end_message = "\n" + name + " will be 100 in the year " + year_at_100 + "!"
print(end_message)

repeat = input("\nHow many times do you want to shout it out to the world? ")

for i in range(int(repeat)):
    print(end_message)