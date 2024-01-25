#The purpose of this program is to take a list and return the first and last elements of that list

def get_first_element(list):
    return list[0]

def get_last_element(list):
    return list[-1]

a = [5, 10, 15, 20, 25]
b = [get_first_element(a), get_last_element(a)]
print(b)