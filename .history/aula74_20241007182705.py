"""
Closure e funções que retornam outras funções:
é uma função + um escopo estendido q contém variáveis livres
"""

def greet(greeting): # função 1: recebe saudação (greeting) como argumento e retorna OUTRA função

    def greetName(name): # função 2: retornada por greeting recebe name e imprime saudação combinada com o nome
        print(greeting, name)
        
    return greetName
    
hello = greet('Hello') # chama greet('Hello') q retorna função greetName com saudação 'Hello' armazenada
hello('Alex')
hello ('Healing')

# impressão:
# Hello Alex
# Helos Healing