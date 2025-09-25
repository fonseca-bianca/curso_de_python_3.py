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

# A função view_list para adicionar e remover
def view_list(task, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task)
    return task_list

# 
task_list = [] # insere tarefa
undo_list = [] # desfaz tarefa
redo_list = [] # refaz tarefa

while True:
    os.system('cls' if os.name =='nt' else 'clear')
    print("Comandos: adicionar, desfazer, refazer")
    comando = input("Digite o comando desejado: ")
    if comando == "adicionar":
        task_list.append("fazer café")
        print(task_list)
        input("Tarefa adicionada. Pressione 'enter' para continuar adicionando")
        task_list.append("caminhar")
        print(task_list)
        input(f"Tarefa adicionada. Sua lista está atualizada: {task_list}")