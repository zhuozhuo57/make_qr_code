import re

# kk = re.compile(r'\d+')
kk = re.compile(r'\d+')
l = re.findall(kk, "\one123m123kk456")
print(l)
