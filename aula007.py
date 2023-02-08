"""
* Criar variavel para nome(str), idade(int),
* altura(float) e peso(float) de uma pessoa
* criar uma variavel com ano atual(int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Dinho'
idade = 41
altura = 1.70
peso = 113
data = 2023
IMC = peso/(altura**2)
print(nome,'nasceu no ano de', (data - idade))
print(f'{nome}, possui o IMC, {IMC:.2f}')
print(f'{nome}, tem, {str(idade)} seu peso atual é, {str(peso)}, possui o IMC de {IMC:.2f}')
