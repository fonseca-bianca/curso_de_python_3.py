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

lista_tarefas = []
desfazer_tarefas = []
refazer_tarefas = []
while True:
    print("\nComandos: listar, desfazer, refazer")
    tarefa = input("Digite uma tarefa que deseja fazer: ")
    if tarefa == "listar":
        print("\nTarefas: ", lista_tarefas)
    elif tarefa == "desfazer":
        desfazer_tarefas.append(lista_tarefas.pop())
    elif tarefa == "refazer":
        lista_tarefas.append(refazer_tarefas.pop())
    else:
        lista_tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")
        refazer_tarefas.clear()  
        