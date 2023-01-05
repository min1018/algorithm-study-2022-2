import re

temp = input()
result = re.sub("C|A|M|B|R|I|D|G|E","",temp)
print(result)