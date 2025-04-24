# Fatiamento de string e função len:

# FUNÇÃO len():
"""OBS.: 
    - quando quiser o 7, incluir o final 8, sempre 1 a mais
    - pq em Python, o início é incluído e o final é excluído
"""
# vai ler a quantidade de caracteres existentes na string, no objeto q 
# tenha o método 'len'

variavel = "Olá mundo"
print(len(variavel))
# output: 9 (conta os espaços tbm)

# FATIAMENTO:
# os ':' é q indicam pro Python q é pra fazer o fatiamento
# [i:f:p] ou [::] (i: início, f: fatiamento, p: pular/passo)
print(variavel[0:9:4])
# output: Omo 
# 0: início
# 9: quantidade total de caracteres (inclusive o espaço)
# 4: quantidade de caracteres q deverá pular até ler o próximo caractere

# [::]: inverte a string
print(variavel[::-1]) # vai contar todos os caracteres da string, mas 
# vai começar de trás pra frente, pq é negativo
# output: odnum álO

# ou

print(variavel[-1:-10:-1])
# output: odnum álO