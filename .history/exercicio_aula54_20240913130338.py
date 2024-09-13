"""Exercício com lista
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
NÃO permita q o programa quebre com erros de índices inexistentes na lista
"""

lista_compras = []

while True:
    print("Selecione uma opção: ")
    opcao = input("(i)nserir | (a)pagar | (l)istar: ").strip().lower()
    if len(opcao) > 1:
        print("Digite somente uma opção por vez")
        continue