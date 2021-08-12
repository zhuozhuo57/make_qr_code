import re

kk = re.compile(r'\d+')
l = re.findall(kk, "one123")
print(l)
