import re

# The pipe symbol matches R1 or R2 when found in a list.
hero_regex = re.compile(r'Batman|Tina Fey')

# It returns whichever regex appears first in the string and short circuits.
mo1 = hero_regex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = hero_regex.search("Tina Fey and Batman")
print(mo2.group())
