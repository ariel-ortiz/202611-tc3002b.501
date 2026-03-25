import re

expreg = r'\w+(?:(o)|(a))\b'
m = re.fullmatch(expreg, 'niña')
if m:
    print(m.span())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
