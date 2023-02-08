#  Operadores Lógico and, or, not, in e not in

#comparacao1 = 2
#comparacao2 = 2
# (verdadeiro E verdadeiro) = verdadairo
# (verdadeiro E False) = False

#comparacao1 and comparacao2

#nome = 'Elizandro'

#if 'sdsd' not in nome:
#    print('Não Existe. ')
#else:
#    print('existe o texto')

usuario = input('Digite seu Usuario: ')
senha = input('Digite sua senha: ')

usuario_bd = 'Dinho'
senha_bd = '1234'

if usuario_bd == usuario and senha_bd == senha:
    print("Voce esta logado!")
else:
    print('usuario ou senha invalidos! ')

