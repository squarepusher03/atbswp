import re


message = "Call me at 415-555-1011 tomorrow."
phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_num_regex.search(message)
print("Phone number found: " + mo.group())
