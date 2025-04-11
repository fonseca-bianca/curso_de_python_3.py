print(12, 34, sep="-")
#sep: Separador. Refere-se ao argumento nomeado
#end: Finalizador. Refere-se ao argumento nomeado
print(12, 34, sep="-", end="*")
print(56, 78, sep='.', end='##')
print()
print()

#\r: Caractere de retorno. Faz com que o cursor volte pro início da linha
print("Olá, mundo", end="\r")
#\n: Caractere de nova linha. Faz com que o cursor vá pra linha seguinte
print(9, 0, sep='.')
# output: 9.0, mundo
print(9, 0, sep=' ')
