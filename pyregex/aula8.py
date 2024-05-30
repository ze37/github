# \w e o mesmo que => [a-zA-Z0-9À-ú]
# /W [^a-zA-z0-9_]
# /d [0-9]
# /D [^0-9]
# \s [ \r\n\f\t]
# \b borda
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
# print(re.findall(r'[a-z]+', texto))
# print(re.findall(r'[a-z]+', texto))

 
 # print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
#print(re.findall(r'\d+', texto, flags= re.I))

# print(re.findall(r'\D+', texto, flags= re.I))
# print(re.findall(r'\s+', texto, flags= re.I)) pega todas as palavras
print(re.findall(r'\be\w+', texto, flags= re.I)) # borda pega todas as  pega todas as palavras que começa com e
# print(re.findall(r'\w+e\b', texto, flags= re.I))
print(re.findall(r'\w+e\b', texto, flags= re.I)) # pega todas as palavras que termina com e
