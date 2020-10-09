import re


# Parenthesis group regex sequences together.
phone_num_regex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phone_num_regex.search('My number is (415) 555-4242.')

# .group() and .group(0) are the same, they return the
# whole string to search from.
print(mo.group())
print(mo.group(0))

# Groups are indexed starting at 1.
print(mo.group(1))
print(mo.group(2))

# .groups() returns all of the groups in the search in a tuple.
print(mo.groups())

# .groups()'s tuple can be unpacked into variables.
area_code, main_number = mo.groups()
print("Area code: "+area_code)
print("Main number: "+main_number)
