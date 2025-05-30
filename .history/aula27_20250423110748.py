# Fatiamento de string e função len:

# função len:
# vai ler a quantidade de caracteres existentes na string, no objeto q 
# tenha o método 'len'
variavel = "Olá mundo"
print(len(variavel))
# output: 9 (conta os espaços tbm)

# Fatiamento
# [i:f:p] [::]
print(variavel[0:9:4])
# 0: início
# 9: quantidade total de caracteres (inclusive o espaço)
# 4: quantidade de caracteres q deverá pular até ler o próximo caractere

# [::]: inverte a string
print(variavel[::-1]) # vai contar todos os caracteres da string, mas 
# vai começar de trás pra frente, pq é negativo
# ou
print(variavel[-1:-10:-1])