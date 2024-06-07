nome = input ("Digite o seu nome completo: ")
idade = input ("Digite sua idade: ")
contem_espaco = " "

if nome and idade:
    if contem_espaco in nome:
        print(f"Seu nome {nome} contém espaços. {contem_espaco}")
    else:
        print(f"Seu nome {nome} não contém espaços.")
print(f"Seu nome é {nome}")
print(f"Seu nome invertido é {nome[::-1]}")
print(f"Seu nome contém" ,(len(nome)), "letras.")
print(f"A primeira letra do seu nome é {nome[0]}")
print(f"A última letra do seu nome é {nome[]}")

else:
    print(f"Desculpe, você deixou campos vazios.")
    
    


