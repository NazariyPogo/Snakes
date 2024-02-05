#The purpose of this program is to take an input integer an output a true or false for whether it is in a random list or not

import random
import code_snippets

def generate_rand_sorted_int_list(nums):
    res = []
    for _ in range(random.randint(1, nums)):
        res.append(random.randint(1, 100))
    res = code_snippets.insertion_sort_bin(res)
    return res

def binary_search(list, key):
    start = 0
    end = len(list)

    while True:
        middle = (end+start) // 2

        if middle < start or middle > end or middle < 0:
            return False

        if list[middle] == key:
            return True
        elif list[middle] > key:
            end = middle
        else:
            start = middle
        
        if middle == (end+start)//2:
            return False

if __name__ == "__main__":
    rand_list = generate_rand_sorted_int_list(30)

    print(f"A randomized list has been made:\n{rand_list}")
    inp = code_snippets.get_user_int_in_range(1, 100, "Please enter a number to see if it is in the randomized list: ")

    print(binary_search(rand_list, inp))