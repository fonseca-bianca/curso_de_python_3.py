primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

# # Convertendo os inputs para números, já q a função input SEMPRE lê tipo string
primeiro_valor = float(primeiro_valor)
segundo_valor = float(segundo_valor)

# if primeiro_valor > segundo_valor:
#     print(f"{primeiro_valor=} é maior que o {segundo_valor=}")
# elif primeiro_valor < segundo_valor:
#     print(f"{segundo_valor=} é maior que o {primeiro_valor=}")
# else:
#     print(
#       f"{primeiro_valor = } é igual ao {segundo_valor = }, "   
#       f"portanto, ambos os valores digitados são iguais"
#   )  

# Outra forma de fazer o exercício acima é quebrando a f'string em partes:
# primeiro_valor = input("Digite o primeiro valor: ")
# segundo_valor = input("Digite o segundo valor: ")
if primeiro_valor >= segundo_valor:
    print(
        f"{primeiro_valor = } é maior ou "
        f"igual ao {segundo_valor = }"
    )
elif primeiro_valor <= segundo_valor:
    print(
        f"{segundo_valor = } é maior "
        f"do que o {primeiro_valor = }"
    )
    
# Nesta forma de fazer o exercício: 
# else:
#     print("Ambos valores digitados são iguais"
#     )
# --------------------------------------------------
# NÃO precisa do 'else', porque:
#   *Se primeiro_valor for maior ou igual, entra no if.
#   *Se for menor ou igual, entra no elif.
#   *⚠️ Mas "igual" se encaixa nas duas! Então:
#   *Se os valores forem iguais, eles já vão satisfazer a condição do if e 
#       nunca vão chegar no else.
#   *Portanto, se quiser que o 'else' seja lido pelo programa, é necessário fazer
#       como no primeiro caso de resolução.

