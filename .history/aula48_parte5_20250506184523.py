"""CUIDADO com os tipos de Dados Mutáveis: list e copy
uso sinal = : copiando o valor (Imutável)
uso sinal = : aponta pro mesmo valor na memória (Mutável)
"""
nome1 = "Ana"
outra_variavel = nome1
nome1 = "João"
print(nome1) # João. Tem um id na memória do programa 
print(outra_variavel) # Ana. Tem outro id na memória do programa


# uso sinal = : aponta pro mesmo valor na memória (Mutável)
lista_a = ["João", "Maria"]
lista_b = lista_a 

lista_a[0] = "Mexe na lista_a e altera o mesmo valor na lista_b" 
# pq ambas apontam pro mesmo valor na memória"
print(lista_b)

# utilizando método 'copy'
lista_a = ["João", "Maria", "Tyrion"]
lista_b = lista_a.copy() # retornar os valores da 'lista_a' pra 'lista_b' 
# (lá no print)

lista_a[0] = "Missandre" # pq ambas apontam pro mesmo valor na memória"
print(lista_a) # imprime 'lista_a' 
print(lista_b) # imprime 'lista_b' com efeito do método 'copy'