"""
Closure e funções que retornam outras funções:
é uma função + um escopo estendido q contém variáveis livres
É uma função definida no escopo de outra função e, por isso, possui acesso
ao contexto e às variáveis da função-PAI/MÃE. É como se ela lembrasse do 
escopo léxico onde foi criada.
Função-FILHA é tratada como OBJETO da Função-MÃE e mantém o estado de variável
externa mesmo APÓS a função-MÃE ter sido executada.
Em Python, funções são tratadas como Primeira Classe (first-class objects), o 
q significa q podem ser passadas como argumentos, atribuídas a variáveis, e 
retornadas de outras funções.
Criação de uma função q se adapta a diferentes valores passados no momento da
execução. 
funções mais dinâmicas e reutilizáveis, permitindo que os parâmetros sejam 
fornecidos posteriormente.
"""

# exemplo 1:
def greet(greeting): 
    # função 1: recebe greeting como argumento e retorna OUTRA função

    def greetName(name): 
        # função 2: retornada por 'greeting' recebe 'name' e imprime saudação 
        # combinada com o nome
        print(greeting, name) 
        # função 2 imprime a saudação(greeting) + nome(name)
        # Como 'greetName' está DENTRO de 'greet', 'greetName' pode acessar o 
        # valor de 'greeting' q foi passado pra 'greet'
        
    return greetName # aq é o retorno de 'greet' com OUTRA função q é 
    # a 'greetName'
    # Quando greet é chamada, ela NÃO executa nada imediatamente, mas 
    # cria e devolve a função 'greetName', q ainda "lembra" o valor de
    # 'greeting'
    
hello = greet('Hello') 
# chama 'greet('Hello')' q retorna função 'greetName' com saudação 'Hello' 
# armazenada
hello('Alex') #'hello' passa a ser a função 'greetName' q foi retornada
hello ('Healing')

# impressão:
# Hello Alex
# Helos Healing

print("--------------------------------")

# exemplo 2:
"""Aq o retorno da função 'multiplicador', q pode receber qlqe valor para 'x', 
e o valor de 'n' é "lembrado" pela função:
"""
def multiplicar_por_n(n):
    def multiplicador(x):
        return x * n  # 'n' foi capturado pela closure
    return multiplicador  # retorna a função

# Aqui você define 'n' como 3
multiplicar_por_3 = multiplicar_por_n(3)

# Depois, passa o valor 'x' para multiplicar
print(multiplicar_por_3(10))  # Output: 30

print("--------------------------------")

# exemplo 3:
def create_greeting2(greeting2):
    def greet2(name2):
        return f"{greeting2}, {name2}"
    return greet2

say_good_morning = create_greeting2("Bom dia")
say_good_night = create_greeting2("Boa noite")

for name2 in ["Maria", "João", "José"]:
    print(say_good_morning(name2))  
    print(say_good_night(name2))  
    