"""Alterando lista (tipo list)
em listas, o ideal é tentar mexer sempre no final dela, considerando listas 
muito grandes, se for alterar algum índice do início ou meio dela, pode 
comprometer o processamento do programa, pq o Python vai precisar usar 
muita memória
"""

minha_lista = [1, 2, 3, 4]
# numero = minha_lista[3]
minha_lista.append(50) # [1, 2, 3, 4, 50]
minha_lista.pop() # remove o 50  ➜ [1, 2, 3, 4]
minha_lista.append("BB") # [1, 2, 3, 4, "BB"]
ultimo_valor = minha_lista.pop() # remove "BB" e armazena ➜ [1, 2, 3, 4]
ultimo_valor = minha_lista.pop(1) # remove o índice 1, que é o
# número 2 ➜ [1, 3, 4]
print(minha_lista, "Removido:", ultimo_valor)  
del minha_lista[-1]
print(minha_lista) 