"""Alterando lista (tipo list)
em listas, o ideal é tentar mexer sempre no final dela, considerando listas muito
grandes, se for alterar algum índice do início ou meio dela, pode comprometer
o processamento do programa, pq o Python vai precisar usar muita memória
"""

minha_lista = [1, 2, 3, 4]
#numero = minha_lista[3]
minha_lista.append(50)
minha_lista.pop() #remove último elemento da lista. tbm retorna um valor q foi removido, se precisar
minha_lista.append("BB")
ultimo_valor = minha_lista.pop() # o "pop", neste caso, está removendo uma string "BB"
ultimo_valor = minha_lista.pop(1) 
print(minha_lista, "Removido:", ultimo_valor)   