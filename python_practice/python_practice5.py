#The purpose of this program is to have a list of all common elements in two separate lists of varying length

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = []
x = []
y = []
custom_result = []
one_liner_result = []

x_size = random.randint(1, 20)
y_size = random.randint(1, 20)

for i in range(x_size):
    x.append(random.randint(0, 100))
x.sort()

for i in range(y_size):
    y.append(random.randint(0, 100))
y.sort()

for i in a:
    if i in b and i not in result:
        result.append(i)

for j in x:
    if j in y and j not in custom_result:
        custom_result.append(j)

print("List x is: ", x)
print("List y is: ", y)
print(f"The common elements are: {custom_result}")
print("The preset lists' common elements are: ", result)

print("The one line attempt yielded this as a response: ", list(set(x) & set(y)))    #The '&' operator can be used in sets to mean 'intersection just like '|' is 'union'