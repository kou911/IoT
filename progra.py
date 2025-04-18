import re
import pyperclip

code = ""

st = pyperclip.paste().split("\n")

for i in st:
 code += (i[re.match(r"[0-9]+",i).end():]+"\n").lstrip()

pyperclip.copy(code)