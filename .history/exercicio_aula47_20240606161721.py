nome = input ("Digite o seu nome (sem sobrenome): ")
idade = input ("Digite sua idade: ")
#contem_espaco = " "

if nome and idade:       
    print(f"Seu nome é {nome}.")
    print(f"Seu nome invertido é {nome[::-1]}.")   
    
    if " " in nome:
        print(f"Seu nome contém espaços.")
    else:
        print(f"Seu nome não contém espaços.")
    #remoção dos espaços antes de começar a contar as letras  
    #remove primeiro argumento (" " = espaço) pelo segundo argumento ("" = string vazia)
    #transformamos string 'nome' em string 'nome_sem_espaco' com espaços removidos  
    nome_sem_espaco = nome.replace(" ", "")
    print(f"Seu nome contém", (len(nome_sem_espaco)), "letras.")
    
    print(f"A primeira letra do seu nome é {nome[0]}.")
    print(f"A última letra do seu nome é {nome[-1]}.")
else:
    print(f"Desculpe, você deixou campos vazios.")
    
    


