primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

# # Convertendo os inputs para números, já q a função input SEMPRE lê tipo string
# primeiro_valor = float(primeiro_valor)
# segundo_valor = float(segundo_valor)

# if primeiro_valor > segundo_valor:
#     print(f"{primeiro_valor=} é maior que o {segundo_valor=}")
# elif primeiro_valor < segundo_valor:
#     print(f"{segundo_valor=} é maior que o {primeiro_valor=}")
# else:
#     print(f"ambos os valores digitados são iguais")
    

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
else:
    print(
        f"{primeiro_valor = } {segundo_valor = } "
        f"ambos os valores digitados são iguais"
    )