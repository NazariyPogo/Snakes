#This file contains random snippets of code ready for copy/pasting to avoid rewriting the same useful code everytime

import random

#Code used to take repeatedly as a user for input and make sure it is an integer
def get_user_input(request_text):
    while True:
        decision = input(request_text)
        if decision.isdigit():
            decision = int(decision)
            return decision
        else:
            print("That is an invalid input, please enter a whole number!")

def get_user_int_in_range(bot, top, request_text):
    while True:
        decision = input(request_text)
        if decision.isdigit():
            decision = int(decision)
            if decision >= bot and decision <= top:
                return decision
            else:
                print(f"That is an invalid input, please enter a whole number between {bot} and {top}!")
        else:
            print(f"That is an invalid input, please enter a whole number between {bot} and {top}!")

def get_user_input_yn(request_text):
    while True:
        decision = input(request_text)
        if decision.lower() == 'y':
            return True
        elif decision.lower() == 'n':
            return False
        else:
            print("That is an invalid input, please enter a whole number!")

def insertion_sort(list):
    l = len(list)

    if l == 1:
        return

    for cur in range(l):
        if cur+1 < l and list[cur] > list[cur+1]:
            sort_swap(list, cur, cur+1)
            for y in reversed(range(len(list[0:cur]))):
                if list[y] > list[y+1]:
                    sort_swap(list, y, y+1)
                break
        break

############################ (I like mine more)

def insertionSortBorrowed(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

############################

def sort_swap(list, index_a, index_b):
    temp = list[index_a]
    list[index_a] = list[index_b]
    list[index_b] = temp

############################ Borrowed binary insertion sort:

def binary_sort(list, key, start, end):
    if start == end:
        if list[start] > key:
            return start
        else:
            return start+1
        
    if start > end:
        return start
 
    mid = (start+end)//2
    if list[mid] < key:
        return binary_sort(list, key, mid+1, end)
    elif list[mid] > key:
        return binary_sort(list, key, start, mid-1)
    else:
        return mid

def insertion_sort_bin(list):
    for i in range(1, len(list)):
        key = list[i]
        loc = binary_sort(list, key, 0, i-1)
        list = list[:loc] + [key] + list[loc:i] + list[i+1:]
    return list

############################

if __name__ == "__main__":

#Tests for insertion sort
    # test_list = [12, 11, 13, 5, 6]
    # test_list2 = []
    # for _ in range(random.randint(1,50)):
    #     test_list2.append(random.randint(1,50))
    # insertion_sort(test_list)
    # insertion_sort(test_list2)
    # print(test_list)
    # print(test_list2)



    pass