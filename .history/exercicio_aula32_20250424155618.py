"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")
try:
    numero = int(numero) # aceita receber somente numero inteiro 
    if numero % 2 == 0:
        print(f"O numero {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except:
    print(f"Você digitou um número que não é do tipo inteiro.")
    
# no exercício acima, poderia usar .isdigit() pra verificar se o número é 
# inteiro ou não, mas o ideal é usar o try/except
   
print(20 * "-") 
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual = input("Digite a hora atual (HH:mm): ")
horas, minutos = map(int, hora_atual.split(':')) # recebendo string do 
# usuário e transformando-a em HH:mm (split) e convertendo pra inteiro

if (horas >= 0 and horas < 12):
    print("Bom dia!")
elif (horas == 12 and minutos == 0) or (horas >= 12 and horas < 18):
    print("Boa tarde!")
else:
    print("Boa noite")

print(20 * "-") 
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 
letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, 
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""nesse tipo de problema, o ideal é conferir primeiro se o usuário digitou um
nome válido e não uma letra solta, por exemplo
"""

nome_usuario = input("Digite o seu primeiro nome: ")
# tamanho_nome = len(nome_usuario) # outra forma de resolver
# if tamanho_nome <= 1: 
#     print("Digite um nome válido com, pelo menos, mais de uma letra")
# elif tamanho_nome <= 4:
#     print("Seu nome é curto ")
# elif tamanho_nome == 5 or tamanho_nome <= 6:
#     print("Seu nome é normal")
# else:
#     print("Seu nome é muito grande")

if nome_usuario is None:
    print("Você precisa digitar um nome")

else:
    print(f"O seu nome {nome_usuario} possui {len(nome_usuario)} letras")

# outra forma de resolver:
# tamanho_nome = len(nome_usuario)
# tamanho_nome: vai devolver um INTEIRO

# aí ficaria:
# if tamanho_nome <= 1:
#     if tamanho_nome ...



