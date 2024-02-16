#The purpose of this program is to identify all overlapping numbers in two separate files.

import time

if __name__ == "__main__":
    start = time.time()
    overlap_nums = []
    iterator_count = 0

    with open('./Supplementary Files/primenumbers.txt', 'r') as open_file:
        line = open_file.readline()
        with open('./Supplementary Files/happynumbers.txt', 'r') as open_file_happy:
            line_happy = open_file_happy.readline()
            while line:
                while line_happy:
                    if int(line_happy) > int(line):
                        break
                    elif int(line) == int(line_happy):
                        overlap_nums.append(int(line))
                    iterator_count += 1
                    line_happy = open_file_happy.readline()
                line = open_file.readline()

                open_file_happy.seek(0)        #Restarts happy number file
                line_happy = open_file_happy.readline()
    
    end = time.time()
    print(overlap_nums)
    print(f"This program ran for: {end - start} seconds")
    print("There were %s iterations of comparison in this process." % (iterator_count))