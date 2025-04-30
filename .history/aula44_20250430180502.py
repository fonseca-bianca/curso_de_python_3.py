"""Função range():
- é iterável
- Range + for: para usar intervalos de números
- range(start, stop, step) 
    ex.: range(5, 10, 2):
            inicio (inclusivo) = 5 
            fim (exclusivo)= 10
            step/passo = 2
- Pode índices NEGATIVOS: 
    ex.: numeros = range(0, -3, -2) 
    ---> Output: 0, -2) 
"""

numeros = range(1, 10, 2) # de 1 a 10, pulando de 2 em 2
# numeros = range(5, 10)
# numeros = range(5, 10, 2)
# print(numeros)

for numero in numeros:
    print(numero)
    
print(20*"-")

# com números negativos:
numeros_b = range(0, -3, -2)
for numero in numeros_b:
    print(numero)
    # Output: 0, -2 (pq -3 é final exclusivo, logo, será -2 o final) 

print(20*"-")

# tabuada:
tabuada_do_oito = range(0, 81, 8)
for numero in tabuada_do_oito:
    print(numero)
    

# múltiplo de 6:
multiplo_de_seis = range(0, 100, 6)
for numero in multiplo_de_seis:
    print(numero)

    
