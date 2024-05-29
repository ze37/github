#  Metacarectere ^ $
# ^ comerça com
# $ começa com
# [^a-z] negação

import re


cpf = '134.547.362-32'

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf))
print(re.findall(r'[^a-z]+',cpf))
 
