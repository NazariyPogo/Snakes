#The purpose of this program is to take a list and to return only the even elements of it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
res = [num for num in a if num % 2 == 0]    #First num is the way the output is organized
print(res)

#More complex use:
x = [1,2,3,4]
y = [1,2,3,4]

print([(i, j) for i in x for j in y if i != j]) #Print a list pairs taking one item from each list one-by-one
                                                #without taking a pair where both numbers are the same