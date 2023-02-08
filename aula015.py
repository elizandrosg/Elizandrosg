'''
formatando valores com modificadores

:s - Texto (Strings)
:d - Inteiros (int)
:f - Numero com pontos Flutuantes (float)
:. (numero)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ˆ) (QUANTIDADE) (TIPO -s, d ou f)
> - Esquerda
< - Direita
ˆ- Centro
'''
"""
num_1 = 10
num_2 = 3
divisao = num_1/num_2

print( '{:.2f}'.format(divisao))
"""
"""
num_1 = 1
print(f'{num_1:0>10}')
"""
#num_2 = 1150
#print(f'{num_2:1>10.2f}')

nome = 'Elizandro'
sobrenome = 'Gonçalves'
nome_formatado = '{1:$^30}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.title())#Somente a primeira letra maiuscula
print(nome.upper())#Todas as letras maiuscula
print(nome.lower())#Todas as letras minuscula


#print(len(nome))
#print(f'{nome:#^33}')
