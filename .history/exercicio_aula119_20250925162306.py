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

# a função view_list para adicionar UMA ÚNICA tarefa
# ela é usada para ADICIONAR uma tarefa ao final da lista
def view_list(task, task_list=None):
    if task_list is None:
        task_list = []
    task_list.append(task)
    return task_list

# --- Listas (Váriaveis Globais do Programa) ---
task_list = []  # lista principal de tarefas
undo_list = []  # lista de tarefas desfeitas (para o refazer)


def listar_tarefas(lista):
    """Função auxiliar para listar tarefas."""
    if not lista:
        print("A lista está vazia.")
        return
    print("\n--- Lista de Tarefas ---")
    for i, tarefa in enumerate(lista):
        # f-string formatada para mostrar a posição e o item
        print(f"{i + 1}. {tarefa}")
    print("------------------------\n")


# --- Loop Principal ---
while True:
    # Limpa o console para melhor visualização
    os.system('cls' if os.name == 'nt' else 'clear') 
    listar_tarefas(task_list)
    print("Comandos: inserir, desfazer, refazer, sair")
    
    # 1. Recebe o comando do usuário
    comando = input("Digite o comando (inserir, desfazer, refazer, sair): ").lower() 

    # --- INSERIR ---
    if comando == "inserir":
        # Pede ao usuário o NOME da tarefa a ser inserida
        nova_tarefa = input("Qual tarefa você deseja inserir? (Ex: fazer café, caminhar): ")

        # Chama sua função original para adicionar a tarefa
        task_list = view_list(nova_tarefa, task_list)
        
        # Exibe a lista atualizada
        print(f"\nTarefa '{nova_tarefa}' inserida!")
        listar_tarefas(task_list)
        input("Pressione 'enter' para continuar.")


    # --- DESFAZER ---
    elif comando == "desfazer":
        if not task_list:
            print("\nNada para desfazer. A lista está vazia.")
            input("Pressione 'enter' para continuar.")
            continue # Volta para o início do loop

        # 1. Remove a ÚLTIMA tarefa (pop)
        tarefa_desfeita = task_list.pop() 
        
        # 2. Guarda a tarefa removida na lista de "desfazer"
        undo_list.append(tarefa_desfeita)
        
        print(f"\nTarefa '{tarefa_desfeita}' desfeita.")
        listar_tarefas(task_list)
        input("Pressione 'enter' para continuar.")


    # --- REFAZER ---
    elif comando == "refazer":
        if not undo_list:
            print("\nNada para refazer. Nenhuma tarefa foi desfeita.")
            input("Pressione 'enter' para continuar.")
            continue

        # 1. Pega a ÚLTIMA tarefa desfeita (pop)
        tarefa_refeita = undo_list.pop() 
        
        # 2. Adiciona de volta à lista principal
        task_list = view_list(tarefa_refeita, task_list) 
        
        print(f"\nTarefa '{tarefa_refeita}' refeita!")
        listar_tarefas(task_list)
        input("Pressione 'enter' para continuar.")


    # --- SAIR ---
    elif comando == "sair":
        print("\nPrograma finalizado.")
        break
        
    # --- COMANDO INVÁLIDO ---
    else:
        print("\nComando inválido. Por favor, use 'inserir', 'desfazer', 'refazer' ou 'sair'.")
        input("Pressione 'enter' para continuar.")