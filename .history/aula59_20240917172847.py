"""
Desempacotamento em chamadas:
chamadas de métodos e funções

Sobre o Resto *_ (NÃO é possível acessar um índice, somente toda a lista):
O operador * em Python, usado para desempacotamento, cria uma nova lista
(ou outro iterável). Coleta todos os valores restantes em uma lista ou outra 
estrutura iterável, mas não pode ser utilizado diretamente para acessar índices 
dessa lista coletada. A razão para isso é que * é um operador de expansão de 
argumentos, e seu propósito é coletar múltiplos valores em uma estrutura iterável, 
não para acessar diretamente elementos de uma estrutura após a coleta.
Somente é possível acessar um índice específico com o resto se ele for declarado 
como uma variável
"""

string_letra = "ABCD"
lista_nomes = ["Amy Lee,", "Kurt Cobain", "Axl Rose,", 1, 2, 3, "Whitney Houston"]
tupla_frase = "Python", "é", "legal"
lord_of_rings = [
    ["Gendalf", "Sam"], # índice 0 da lista de dentro
    ["Sauron", "Galadriel", "Frodo"], # índice 1 da lista de dentro
    ["Piki"] # índice 2 da lista de dentro
]


"""a, b, c, *_ = lista_nomes # itens da lista (Amy Lee, Kurt Cobain, Axl Rose)
print(a, c, *_) # a = Amy Lee, c = Axl Rose, *_ (resto) = vai imprimir 1,2,3 como uma única lista


a, b, *_, u = lista_nomes
print(a, u)
"""

# for nome in lista_nomes:
#     print(nome)
    
# print(*lista_nomes)
# print(*string_letra)
# print(*tupla_frase)

print(*lord_of_rings) # remove os colchetes pq está sendo passada lista por lista pra dentro do print (como se cada lista fosse um valor)