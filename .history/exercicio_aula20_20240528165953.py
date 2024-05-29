primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

# Convertendo os inputs para números, já q a função input SEMPRE lê tipo string
# primeiro_valor = float(primeiro_valor)
# segundo_valor = float(segundo_valor)

if (primeiro_valor > segundo_valor):
    print(f"primeiro_valor= '{primeiro_valor}' é maior que o segundo_valor= '{segundo_valor}'")
elif (primeiro_valor < segundo_valor):
    print(f"segundo_valor= '{segundo_valor}' é maior que o primeiro_valor= '{primeiro_valor}'")
else:
    print(f"ambos os valores digitados são iguais")
    