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

print(to_do_list)   


   
# desfazer a tarefa que estiver na lista: 
desfazer_tarefa = []
if to_do_list:
    tarefa_desfeita = to_do_list.pop()
    desfazer_tarefa.append(tarefa_desfeita)

print(f"Lista de tarefas atualizada: {to_do_list}")



while True:
    user_command = input("Digite um comando (listar, desfazer, refazer, sair) ou uma nova tarefa: ")
    
    if user_command == 'listar':
        listar_tarefas()
        continue # Volta para o início do loop

    if user_command == 'desfazer':
        if not to_do_list:
            print("Nada para desfazer.")
            continue
        
        tarefa_desfeita = to_do_list.pop()
        desfeitas.append(tarefa_desfeita)
        print(f"Tarefa '{tarefa_desfeita}' desfeita.")
        listar_tarefas()
        continue

    if user_command == 'refazer':
        if not desfeitas:
            print("Nada para refazer.")
            continue
        
        tarefa_refeita = desfeitas.pop()
        to_do_list.append(tarefa_refeita)
        print(f"Tarefa '{tarefa_refeita}' refeita.")
        listar_tarefas()
        continue

    if user_command == 'sair':
        print("Saindo...")
        break

    # Se o comando não for reconhecido, trate como uma nova tarefa
    to_do_list.append(user_command)
    print(f"Tarefa '{user_command}' adicionada.")
    listar_tarefas()