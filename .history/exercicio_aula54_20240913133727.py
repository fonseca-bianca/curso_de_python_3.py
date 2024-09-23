"""Exercício com lista
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
NÃO permita q o programa quebre com erros de índices inexistentes na lista
"""
import os

lista_compras = []

while True:
    print("Selecione uma opção: ")
    opcao = input("(i)nserir | (a)pagar | (l)istar: ").strip().lower()
    
    if len(opcao) > 1:
        print("Digite somente uma opção por vez")
        continue
    
    if opcao == "i":
        os.system("cls")
        item_adicionado = input("Adicione o item na lista:")
        lista_compras.append(item_adicionado)
        
    elif opcao == "a":
        item_adicionado = input("Escolha o item da lista que deseja apagar: ")
        
        try:
            indice = int(item_adicionado)
            del lista_compras[indice]
        except ValueError as indice:
            print(f"O item '{item_adicionado}' não foi encontrado na lista")
    
    elif opcao == "l":
        os.system("clear")
        
        if len(lista_compras) == 0:
            print("Não há itens da lista")
        
        for i, item_adicionado in enumerate(lista_compras):
            print(f"{i}, {item_adicionado}")
        
        