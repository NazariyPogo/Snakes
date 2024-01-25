#The purpose of this program is to take all non-duplicate common elements from two lists and to save them in a separate list, this must be done in one line of code.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Answer should be [1, 2, 3, 5, 8, 13]

# c = list(set(a) & set(b))
# print(c)

# d = list(set([i for i in a if i in b]))
# print(d)

result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
print(result)

#This assignment is dumb because the instructions make it seem harder than it is or I am doing something not by the rules