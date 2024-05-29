# Meta Caracteres ^ $

# [@#a-zA-Z0-9] isso é um conjunto
# (abc | def) isso é um grupo

import re
from pprint import pprint
texto = '''
<p>fraze 1</p><p>fraze 2</p><p>fraze 3</p><div>fraze 4</div>
'''
cpf = '134.547.362-32'

pprint(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))
#tags = re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>',texto)
#pprint(tags)

#for tag in tags:
 #   um, dois, tres= tag
  #  print(tres)
