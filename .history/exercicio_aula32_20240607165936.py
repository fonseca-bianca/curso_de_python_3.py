"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")
try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"O numero {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except:
    print(f"Você digitou um número que não é do tipo inteiro.")
    
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual = input("Digite a hora atual: ")

if hora_atual == 0 or hora_atual >= 11:
    print("Bom dia!")
elif hora_atual == 12 or hora_atual >= 17:
    print("Boa tarde!")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""