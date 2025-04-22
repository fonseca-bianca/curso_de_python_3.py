# OPERADORES IN e NOT IN:
nome = "Bianca"
# print(nome[-2]) --> vai imprimir 'c'
print("b" in nome or "B" in nome)

# A expressão ("b" or "B") retorna "b", pq no operador `or`, o 
# Python avalia o primeiro valor.
# Como "b" é uma string não vazia (portanto True), o Python não 
# precisa nem avaliar "B".
# Então, a expressão ("b" or "B") in nome vira: "b" in nome
# Como a string "Bianca" começa com "B" maiúsculo e "b" minúsculo 
# NÃO está em "Bianca", o resultado final será False.

print(10 * "-")
print("anc" not in nome)

sobrenome = input("Digite o seu sobrenome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar.upper() in sobrenome:
    print(f"{encontrar} está em {sobrenome}")
else:
    print(f"{encontrar} não está em {sobrenome}")