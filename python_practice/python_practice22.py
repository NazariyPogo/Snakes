#The purpose of this program is to read a file and count the number of items for each 'category'

import code_snippets

def get_cat(line):
    line = str(line).split('/',3)   #Split the entry to parts where there was a '/'
    return line[2]                  #Return the third entry (abbey being taken out in the first run)

if __name__ == "__main__":
    cat_dict = {}
    with open('./Supplementary Files/Training_01.txt', 'r') as open_file:
        line = open_file.readline()
        while line:
            cat = get_cat(line)
            if not cat in cat_dict:
                cat_dict[cat] = 1
            else:
                cat_dict[cat] += 1
            line = open_file.readline()

    for key in cat_dict:
        print(f"{key} : {cat_dict[key]}")