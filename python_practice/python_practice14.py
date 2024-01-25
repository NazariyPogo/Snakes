#The purpose of this program is to take a list and remove any duplicate elements using a function

a = [1,1,2,3,4,5,6,4,3,2,1,7,9,63,53,63,8,7,5,3]

def remove_dups_loop(list):
    res = []
    for elem in list:
        if(elem not in res):
            res.append(elem)
    return res

def remove_dups_sets(list):
    return set(list)

print(remove_dups_loop(a))
print(remove_dups_sets(a))