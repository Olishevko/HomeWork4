import re
some_string = str('я тупой баран, тупой настолько, тупее быть не куда')
print(some_string)
new_some_string = re.sub(r'тупой','',some_string)
print(new_some_string)
