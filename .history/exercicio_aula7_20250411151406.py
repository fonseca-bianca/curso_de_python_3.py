nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
ano_nascimento = 2025 - idade
maior_idade = idade >= 18
altura_metros = float(input("Digite sua altura em metros: " + "m"))


print('Nome', nome)
print('Sobrenome', sobrenome)
print('Idade', idade)
print('Ano nascimento', ano_nascimento)
print('É maior idade?', maior_idade)
print('Altura em metros', altura_metros)

