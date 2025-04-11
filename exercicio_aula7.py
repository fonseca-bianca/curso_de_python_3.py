nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
ano_nascimento = 2025 - idade
maior_idade = idade >= 18
altura_cm = float(input("Digite sua altura em metros (ex.: 175): "))
altura_metros = altura_cm/100 # vai converter a altura de cm para metros

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano nascimento:', ano_nascimento)
print('É maior idade?', maior_idade)
print(f'Altura em metros: {altura_metros:.2f}') 
#:.2f: formata a altura em metros com 2 casas decimais

