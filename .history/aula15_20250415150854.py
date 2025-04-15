""" função INPUT:
- serve pra coletar dados do usuário
- SEMPRE retorna string, mesmo q o usuário digite um número

* nome = input("Digite o seu nome completo: ")
* print(f'O seu nome é {nome}')
"""

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


# Convertendo a string em outro tipo de dado (conversão direta):
digite_numero = int(input("Digite um número: "))
print(f'O número digitado foi: {digite_numero}')

# Podemos atribuir o valor da variável ao nome da variável: útil pra 
# verificar o valor da variável
"""
OBS.: A conversão direta pode causar erros futuros ou até mesmo 'quebrar'
o código na primeira digitação incorreta do usuário. Por isso, é interessante
primeiro receber o dado como string (padrão da função input) e só depois 
realizar a conversão para o tipo desejado (int, float, etc).

Com base no exemplo acima, seria:
digite_numero = input("Digite um número: ") => Recebe o dado como string
conversao_dado = int(digite_numero)         => Converte a string para inteiro
print(f'O número digitado foi: {conversao_dado}')

"""
nome = input("Digite seu nome: ")
print(f'O seu nome é: {nome=}') 
# é o mesmo q, porém, + "limpo" e eficiente: 
# print(f'O seu nome é: nome= {nome}')


digite_numero = input("Digite um número: ") 
conversao_dado = int(digite_numero) 
print(f'O número digitado foi: {conversao_dado}')