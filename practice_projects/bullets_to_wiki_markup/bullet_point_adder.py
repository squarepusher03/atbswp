#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip


text = pyperclip.paste()

# TODO: Separate lines and add stars. @squarepusher03

pyperclip.copy(text)
