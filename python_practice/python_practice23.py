#The purpose of this program is to identify all overlapping numbers in two separate files.

if __name__ == "__main__":
    overlap_nums = []

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
                    line_happy = open_file_happy.readline()
                line = open_file.readline()

                open_file_happy.seek(0)        #Restarts happy number file
                line_happy = open_file_happy.readline()
    
    print(overlap_nums)