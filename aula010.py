#  Operadores Relacionais == igual > maior >= maior igual < menos <= menos igual != diferente

#print( 2 == 2 )

#num_1 = 2  #int
#num_2 = '2'  #str

#print(num_1, num_2)
#print(num_1==num_2)

#expressao = num_1 == num_2

#expressao = num_1 != num_2

#print(expressao)

nome = input('qual seu nome? ')
idade = input('Qual a sua Idade? ')
idade=int(idade)

#  Limite de idade para emprestimo
#idade_limite = 18
idade_menor = 20  #muito jovem
idade_maior = 30  #passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar emprestimo')
else:
    print(f'{nome} NÃO pode pegar emprestimo')

