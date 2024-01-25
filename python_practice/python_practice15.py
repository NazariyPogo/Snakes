#The purpose of this program is to take a user sentence string and return the words in reverse order

initial_string = "My name is Nazariy"

def split_string_by_space(string):
    return str(string).split(' ')

str_list = split_string_by_space(initial_string)
res = ''

for word in str_list[::-1]:
    res += word
    res += ' '
res = res.lstrip()

print(res)