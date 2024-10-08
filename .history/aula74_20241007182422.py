"""
Closure e funções que retornam outras funções:
é uma função + um escopo estendido q contém variáveis livres
"""

def greet(greeting): # função que recebe saudação (greeting) como argumento e retorna OUTRA função

    def greetName(name):
        print(greeting, name)
        
    return greetName
    
hello = greet('Hello')
hello('Alex')
hello ('Healing')