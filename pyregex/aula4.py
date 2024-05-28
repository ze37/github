# Meta caractere . ^ $  [ ] % | ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
import re

texto = '''
<p>fraze 1</p><p>fraze 2</p><p>fraze 3</p><div>fraze 4</div>
'''
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto))
