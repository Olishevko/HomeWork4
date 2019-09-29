import re
phone_number = input('enter phone number: ')
valiad_phone_number = re.sub(r'\D', '', phone_number)
print(valiad_phone_number)
