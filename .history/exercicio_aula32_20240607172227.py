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

hora_atual = input("Digite a hora atual (HH:mm): ")
horas, minutos = map(int, hora_atual.split(':')) #recebendo string do usuário e transformando-a em HH:mm (split) e convertendo pra inteiro

if (horas == 0 and minutos == 0) or (horas >= 0 and horas < 12):
    print("Bom dia!")
elif (horas == 12 and minutos == 0) or (horas >= 12 and horas < 17):
    print("Boa tarde!")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_usuario = input("Digite o seu primeiro nome: ")

if len(nome_usuario) <= 4:
    print(f"Seu nome {nome_usuario} é curto ")