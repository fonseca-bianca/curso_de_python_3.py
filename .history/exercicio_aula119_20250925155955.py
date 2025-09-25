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
        task_list.append([1]"fazer café", [2]"caminhar")
        print(task_list)
        input("Tarefa adicionada. Pressione 'enter' para continuar adicionando")
        input(f"Tarefa adicionada. Sua lista está atualizada é: {task_list}")
    elif comando == "desfazer":
        task_list.remove([1]"fazer café", [2]"caminhar")
        print(task_list)
        input("Tarefa removida. Pressione 'enter' para continuar removendo")
        input(f"Tarefa removida. Sua lista atualizada é: {task_list}")
    elif comando == "refazer":
        task_list.append([1]"fazer café", [2]"caminhar")
        print(task_list)
        input("Tarefa refeita. Pressione 'enter' para continuar refazendo")
        input(f"Tarefa refeita. Sua lista atualizada é: {task_list}")