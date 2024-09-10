minha_lista_a = [1, 2, 3, 4]
minha_lista_b = [5, 6, 7, 8]
resultado_listas = minha_lista_a + minha_lista_b
resultado_listas = minha_lista_a.extend(minha_lista_b)

print(resultado_listas) # retorna None
""" retorna None, pq método .extend() NÃO retorna nada, pq ele 
 vai mexer no valor colocado no objeto. No caso acima, ele vai mexer diretamente
na 'minha_lista_a' """
