#OPERADORES IN e NOT IN:
nome = "Bianca"
#print(nome[-2]) --> vai imprimir 'c'

print("b" in nome or "B" in nome)
#print(("b" or "B") in nome)
# "b" é uma string não vazia, é avaliada como verdadeira, então ("b" or "B") resulta em "b".
# Portanto, a expressão ("b" or "B") in nome se transforma em "b" in nome. Como "b" (minúsculo) 
# não está na string "Bianca", o resultado é False, pois a expressão ("b" or "B") será avaliada
# primeiro, sendo q "b" é True, mas o nome escrito no programa começa com "B", logo
# será tida como False

print(10 * "-")
print("anc" not in nome)

sobrenome = input("Digite o seu sobrenome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in sobrenome:
    print(f"{encontrar} está em {sobrenome}")
else:
    print(f"{encontrar} não está em {sobrenome}")