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
def view_list(task, to_do_list=None):
    if to_do_list is None:
        to_do_list = []
    
    # A lógica para desfazer seria adicionada aqui
    if task == "desfazer":
        removed_task = to_do_list.pop()
        print(to_do_list)
        return to_do_list
    
    # Adiciona a tarefa se não for um comando
    if task not in ("listar", "desfazer", "refazer"):
        to_do_list.append(task)
        print(to_do_list)

    return to_do_list

# Inicializa a lista
to_do_list = []
print("Lista de Tarefas - comandos: listar, desfazer, refazer")

# Loop principal para interação com o usuário
while True:
    user_command = input("Digite uma tarefa, ou um comando (listar, desfazer, sair): ")
    
    # Exibe a lista
    if user_command == "listar":
        print("\n--- Lista de Tarefas ---")
        for tarefa in to_do_list:
            print(f"- {tarefa}")
        print("------------------------\n")
        continue
    
    # Usa a função para adicionar ou desfazer a tarefa
    to_do_list = view_list(user_command, to_do_list)
