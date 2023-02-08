'''
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. caso o usuario nao digite um
nuemro inteiro, informe que não é um numero inteiro.
'''
'''
numero = input('Digite um numero inteiro. ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par.')
    else:
        print(f"{numero} é impar.")
else:
    print('Isso não pe um numero inteiro.')
'''
"""
Faça um programa que pergunte a hora ao usuario e, 
baseando-se no horario descrito, exiba a saudação apropriada. 
Ex. Bom dia 0 - 11, boa tarde 12 - 17, boa noite 18 -23. 
"""
'''
hora = input('Digite o horario atual. ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horario deve estar entre 0 e 23.')

    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Horario deve estar entre 0 e 23.')

'''

'''
Faça um programa que peça o primeiro nome do usuario. 
Se i nome tiver 4 letras ou menos escreva "seu nome é curto",
se tiver entre 5 e 6 letras, escreva "Seu nome é normal",
maior que 6 escreva "Seu nome é muito grande".
'''

nome = input("Digite seu primeiro nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto!")
elif tamanho <= 6:
    print("Seu nome é normal!")
else:
    print("seu nome é grande!")

