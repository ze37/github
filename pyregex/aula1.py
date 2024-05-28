import re

# findall search sub
# compile

string = 'Este e um teste de expressoes regulares' 
print(re.search(r'teste',string))
print(re.findall(r'teste',string))
print(re.sub(r'teste','coisa',string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('cuida',string))
