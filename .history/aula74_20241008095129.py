"""
Closure e funções que retornam outras funções:
é uma função + um escopo estendido q contém variáveis livres
É uma função definida no escopo de outra função e, por isso, possui acesso
ao contexto e às variáveis da função-PAI/MÃE. É como se ela lembrasse do escopo
léxico onde foi criada.
"""

def greet(greeting): # função 1: recebe saudação (greeting) como argumento e retorna OUTRA função

    def greetName(name): # função 2: retornada por 'greeting' recebe 'name' e imprime saudação combinada com o nome
        print(greeting, name) # função 2 imprimindo a saudação(greeting) + nome(name)
        # Como 'greetName' está DENTRO de 'greet', 'greetName' pode acessar o valor de 'greeting' q 
        # foi passado pra 'greet'
        
    return greetName # aq é o retorno de 'greet' com OUTRA função q é a 'greetName'
    # Quando greet é chamada, ela NÃO executa nada imediatamente, mas cria e devolve a 
    # função 'greetName', q ainda "lembra" o valor de 'greeting'.
    
hello = greet('Hello') # chama 'greet('Hello')' q retorna função 'greetName' com saudação 'Hello' armazenada
hello('Alex') #'hello' passa a ser a função 'greetName' q foi retornada
hello ('Healing')

# impressão:
# Hello Alex
# Helos Healing