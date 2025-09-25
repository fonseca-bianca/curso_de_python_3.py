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
import os # usado para limpar a tela

# a função view_list para adicionar UMA ÚNICA tarefa
# ela é usada para ADICIONAR uma tarefa ao final da lista
def view_list(task, task_list=None):
    if task_list is None:
        task_list = [] # lista vazia de tarefas é criada se lista for 'None'
    task_list.append(task)
    return task_list

# listas q são variáveis Globais do programa:
task_list = []  # lista principal de tarefas 
undo_list = []  # lista de tarefas desfeitas (para o refazer)


def listed_tasks(todo_list):
    # função auxiliar pra listar tarefas:
    if not todo_list:
        print("A lista está vazia.")
        return
    print("\n--- Lista de Tarefas ---")
    for i, task in enumerate(todo_list): 
        # enumerate fornece a posição (i) e o item (task) um de cada vez
        # f-string formatada para mostrar a posição e o item
        print(f"{i + 1}. {task}")
    print("------------------------\n")


# loop principal:
while True:
    # limpa o console para melhor visualização:
    if command == 'cls' or command == 'clear':
        os.system('cls' or 'clear') # pra Windows ou Linux
    print("Comandos: inserir, desfazer, refazer, sair")
    
    # 1. recebe o input do usuário:
    command = input("Digite um dos comandos acima: ").lower() 

    # INSERIR:
    if command == "inserir":
        # Pede ao usuário o NOME da tarefa a ser inserida
        new_task = input("Qual tarefa você deseja inserir? "
                         "(Ex: fazer café, caminhar): ")

        # chama a função original pra adicionar a tarefa:
        task_list = view_list(new_task, task_list)
        
        # exibe a lista atualizada:
        print(f"\nTarefa '{new_task}' inserida!")
        listed_tasks(task_list)
        input("Pressione 'enter' para continuar.")


    # DESFAZER:
    elif command == "desfazer":
        if not task_list:
            print("\nNada para desfazer. A lista está vazia.")
            input("Pressione 'enter' para continuar.")
            continue # Volta para o início do loop

        # 1. remove a ÚLTIMA tarefa (pop):
        undone_task = task_list.pop() # armazena o item na variável undone_task
        
        # 2. guarda a tarefa removida na lista de "desfazer":
        undo_list.append(undone_task)
        # adiciona a tarefa q acabou de ser removida (undone_task) na 
        # lista undo_list (pra ela poder ser refeita depois se o usuário quiser)
        
        print(f"\nTarefa '{undone_task}' desfeita.")
        listed_tasks(task_list)
        input("Pressione 'enter' para continuar.")


    # REFAZER:
    elif command == "refazer":
        if not undo_list:
            print("\nNada para refazer. Nenhuma tarefa foi desfeita.")
            input("Pressione 'enter' para continuar.")
            continue

        # 1. pega a ÚLTIMA tarefa desfeita (pop):
        redone_task = undo_list.pop() 
        # remove o último item da lista undo_list e armazena na variável 
        # redone_task (pra ser refeita posteriormente se o usuário quiser)
        
        # 2. adiciona de volta à lista principal:
        task_list = view_list(redone_task, task_list) 
        
        print(f"\nTarefa '{redone_task}' refeita!")
        listed_tasks(task_list)
        input("Pressione 'enter' para continuar.")


    # SAIR:
    elif command == "sair":
        print("\nPrograma finalizado.")
        break
        
    # COMANDO INVÁLIDO:
    else:
        print("\nComando inválido. Por favor, use 'inserir', 'desfazer', 'refazer' ou 'sair'.")
        input("Pressione 'enter' para continuar.")