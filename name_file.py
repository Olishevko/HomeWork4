import re
name_file = str('C:/ProgramData/user/testsite/www/myfile.txt ')
print(name_file)
new_name_file = re.sub(r'.txt', '', name_file)
print(new_name_file)
