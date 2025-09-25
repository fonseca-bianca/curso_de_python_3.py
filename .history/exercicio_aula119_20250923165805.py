"""
Lista de tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']

- se for executar um comando = ação

"""
import os

lista_tarefas = input("Digite a tarefa a ser adicionada: ")

def exibir_lista(tarefa, lista_tarefas=None):
    if lista_tarefas is None:
        lista_tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada à lista")
    return lista_tarefas

# adicionar tarefa à lista:
lista_tarefas = []
tarefa1 = "fazer café"
lista_tarefas = exibir_lista(tarefa1, lista_tarefas)
tarefa2 = "caminhar"
lista_tarefas = exibir_lista(tarefa2, lista_tarefas)
print(lista_tarefas)   
   
# desfazer a tarefa que estiver na lista: 
desfazer_tarefa = []
if lista_tarefas:
    tarefa_desfeita = lista_tarefas.pop()
    desfazer_tarefa.append(tarefa_desfeita)

print(f"Lista de tarefas atualizada: {lista_tarefas}")



