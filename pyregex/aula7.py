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
print(re.findall(r'[a-z]+', texto))
print(re.findall(r'[a-z]+', texto))
print(re.findall(r'[a-z]+', texto))
