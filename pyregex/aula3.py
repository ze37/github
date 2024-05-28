# Meta caractere . ^ $  [ ] % | ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
# {n}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10] Especificamente 10
# () => [a-zA-Z0-9]
# {min, max}
# 
import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano exelente na vida de joao. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele cafe com paode queijo nas tardes de
domingo. Tambemné! Sendo a boa mineira que é, nunca esquece seu famos
pao de queijo.
Nao canso de ouvir a Maria:
"Jooooooooooãoooo o cafe ta protinho aqui. veeeemmm"

'''
print(re.findall(r'jo+ão+',texto, flags=re.I))
print(re.findall(r'jo{1,}.o{1,}',texto, flags=re.I))
print(re.findall(r've{4}m{1,}',texto, flags=re.I))
#print(re.sub(r'jo+.o+','ze',texto, flags=re.I))
