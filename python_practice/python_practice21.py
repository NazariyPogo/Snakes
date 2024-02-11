#The purpose of this program is to write the contents of python_practice20.py into a text file with a name given by the user

import code_snippets

def take_from_file_to_txt(origin_file, end_file):
    data = read_from_file(origin_file)
    save_to_file(end_file, data)

def save_to_file(file_name, data):
    with open(f'./Supplementary Files/{file_name}.txt', 'w') as open_file:
        open_file.write(data)

def read_from_file(file_name):
    with open(f'{file_name}', 'r') as open_file:
        return open_file.read()

if __name__ == "__main__":
    practice_20_filename = './python_practice/python_practice20.py'
    intro_text = "The code for practice 20 looks great! Let's save it to a file, what do you want to name that file?: "

    end_file = code_snippets.get_user_input_text(intro_text)

    take_from_file_to_txt(practice_20_filename, end_file)

    print("The transfer has finished!")