import re

texto = 'Hola, a todos los Isc de este grupo.'
m = re.search('I[ST]C', texto, re.IGNORECASE | re.ASCII)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
else:
    print(m)

m = re.match(r'H\w*', texto)
if m:
    print(m.span())
    print(m.string)
    print(m.group())
else:
    print(m)

for palabra in re.finditer(r'[a-z]+', texto, re.IGNORECASE):
    print(palabra.span(), palabra.group())
