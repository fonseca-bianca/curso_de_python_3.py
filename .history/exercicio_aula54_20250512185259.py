""" Exercício com lista:
Faça uma lista de compras com listas
o usuário deve ter a possibilidade de inserir, apagar e listar valores de sua 
lista NÃO permita q o programa quebre com erros de índices inexistentes na 
lista
"""
import os

lista_compras = [] # inicia a lista de compras vazia

while True: # loop principal (while pq não sabemos quantas vezes o usuário 
    # vai querer adicionar itens)
    print("Selecione uma opção: ")
    opcao = input("(i)nserir | (a)pagar | (l)istar: ").strip().lower() 
    
    if len(opcao) > 1:
        print("Digite somente uma opção por vez")
        continue # volta pro início do programa qndo usuário erra. Qndo acerta,
        # o programa avança
    
    if opcao == "i":
        os.system("cls") # limpa o terminal qndo está no 'i'
        item_adicionado = input("Adicione o item na lista: ")
        lista_compras.append(item_adicionado)
        
    elif opcao == "a":
        item_adicionado = input("Escolha, pelo índice, o item da lista "\
            "que deseja apagar: ")
        
        # tratamento de Exceções:
        try:
            indice = int(item_adicionado) # converte o índice para inteiro
            del lista_compras[indice]
        except ValueError as indice:
            print("Digite um número inteiro.")
        except IndexError as indice:
            print("Índice inexistente.")
        except Exception: # caso o programa caia em um erro q NÃO seja os 
            # erros anteriores
            print("Erro desconhecido.")
    
    elif opcao == "l":
        os.system("cls") # limpa o terminal qndo está no 'l'
        
        if len(lista_compras) == 0:
            print("Não há itens na lista.")
        
        for indice, item_adicionado in enumerate(lista_compras):
            print(f"{indice} - {item_adicionado}")
        
        