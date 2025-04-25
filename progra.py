import re
import pyperclip

code = ""

st = pyperclip.paste().split("\n")

for i in st:
 i = i+"\n"
 code += (i[re.match(r"[0-9]+",i).end():]).lstrip()

pyperclip.copy(code)