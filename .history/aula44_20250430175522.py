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

numeros_b = range(0, -3, -2)
for numero in numeros_b:
    print(numero)
    # Output: 0, -2 (pq -3 é final exclusivo, logo, será -2 o final) 
    
    
