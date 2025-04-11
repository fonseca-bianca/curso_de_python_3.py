print(12, 34, sep="-")
#sep: Separador. Refere-se ao argumento nomeado
#end: Finalizador. Refere-se ao argumento nomeado
print(12, 34, sep="-", end="*\r\n") #\r\n: Caractere de retorno e nova linha. 
print(56, 78, sep='.', end='##')
print()
print()

#CRLF: \r\n
#LF (Unix e MAC): \n
#\r: Caractere de retorno. Faz com que o cursor volte pro início da linha
print("Olá, mundo", end="\r")
#\n: Caractere de nova linha. Faz com que o cursor vá pra linha seguinte
print(9, 0, sep='.')
# output: 9.0, mundo
print(9, 0, sep=' ')
