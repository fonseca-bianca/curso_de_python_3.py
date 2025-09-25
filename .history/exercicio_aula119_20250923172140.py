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

def view_list(task, to_do_list=None):
    if to_do_list is None:
        to_do_list.append(task)
        print(f"Tarefa '{task}' adicionada à lista")
    return to_do_list

# adicionar tarefa à lista:
to_do_list = []
task1 = "fazer café"
to_do_list = view_list(task1, to_do_list)
task2 = "caminhar"
to_do_list = view_list(task2, to_do_list)

   
# desfazer a tarefa que estiver na lista: 
desfazer_tarefa = []
if to_do_list:
    task_undo = to_do_list.pop()
    desfazer_tarefa.append(task_undo)

print(f"Lista de tarefas atualizada: {to_do_list}")



