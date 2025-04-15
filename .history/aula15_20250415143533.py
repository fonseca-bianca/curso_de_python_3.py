# função INPUT serve pra coletar dados do usuário

# nome = input("Digite o seu nome completo: ")
# print(f'O seu nome é {nome}')

numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")

# print(f'A soma dos números é: {numero_1 + numero_2}')
# vai imprimir a concatenação e não a soma, porque a Função INPUT lê o tipo 
# string
# o ideal é fazer uma checagem pra saber se o q o usuário digitou é o q foi 
# solicitado
# pra daí sim realizar a conversão e, posteriormente, a soma

# checagem:
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f"A soma dos números é: {int_numero_1 + int_numero_2}")
