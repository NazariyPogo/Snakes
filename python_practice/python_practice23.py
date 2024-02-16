#The purpose of this program is to identify all overlapping numbers in two separate files.

import linecache
import time

prime_file = './Supplementary Files/primenumbers.txt'
happy_file = './Supplementary Files/happynumbers.txt'

def get_int_line_from_prime(line_num):
    try:
        return int(linecache.getline(prime_file, line_num))
    except:
        return -1

def get_int_line_from_happy(line_num):
    try:
        return int(linecache.getline(happy_file, line_num))
    except:
        return -1

if __name__ == "__main__":
    start = time.time()
    overlap_nums = []
    happy_line_counter = 1                                          #1-based numbering system 
    prime_line_counter = 1
    iter_count_comparisons = 0                                      #For fun to see the number of iterations in each while-loop system
    iter_count_backtracker = 0

    with open(prime_file, 'r') as open_file:                        #Open both files and assign file line based on counter
        line = get_int_line_from_prime(prime_line_counter)
        with open(happy_file, 'r') as open_file_happy:
            line_happy = get_int_line_from_happy(happy_line_counter)


            while line:                                             #Compare current nums from each file
                while line_happy:
                    if line_happy > line:
                        break
                    elif line == line_happy:
                        overlap_nums.append(line)
                    iter_count_comparisons += 1


                    happy_line_counter += 1                         #Get next line from happy file and breaking if file is done
                    line_happy = get_int_line_from_happy(happy_line_counter)
                    if line_happy == -1: break
                prime_line_counter += 1


                line = get_int_line_from_prime(prime_line_counter)  #Get next line from prime file and breaking if line is done
                if line == -1: break


                while line < line_happy:      #Iterate back each line in happy file to avoid restarting file everytime
                    iter_count_backtracker += 1
                    happy_line_counter -= 1
                    line_happy = get_int_line_from_happy(happy_line_counter)

    end = time.time()
    print(overlap_nums)
    print(f"This program ran for: {end - start} seconds")
    print("There were %s iterations of comparison and %s iterations of backtracking in this process." % (iter_count_comparisons, iter_count_backtracker))