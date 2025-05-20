"""
Escopo de funções em Python:
significa o local onde aquele cód poderá atingir
Tipos:
a) Local:
é o escopo onde APENAS nomes do mesmo local podem ser alcançados
b) Global:
é o escopo onde TODO o cód é alcançável
OBS.: com funções, o cód consegue executar comandos em ordens distintas, SEM 
ser sempre da esquerda->direita e de cima->baixo
"""

# Exemplo 1 - Escopo global vs escopo local simples:
z = 1  # Variável no escopo global

def mostrar_variavel_local():
    z = 100  # Essa variável 'z' é local da função, diferente da 'z' global
    print("Dentro da função:", z) # Saída: 100

mostrar_variavel_local()  # Saída: 100
print("Fora da função:", z)  # Saída: 1

print("Exemplo 1 - Escopo simples ---------------------------------------")


# Exemplo 2 - Funções aninhadas (escopos aninhados)
a = 5  # Variável no escopo global

def funcao_externa():
    def funcao_interna():
        b = 10  # Variável local da função interna
        print("Dentro da função interna:", a, b)  # Acessa 'a' (global) e 'b'
        # (local)
    
    funcao_interna()
    print("Dentro da função externa:", a)  # Acessa apenas 'a', pois 'b' está 
    # fora do seu escopo

funcao_externa()

# OBS: A função externa não acessa 'b' da interna, mas a interna acessa 'a' 
# da externa/global

print("Exemplo 2 - Funções aninhadas -------------------------------------")


# Exemplo 3 - Escopo com variáveis de mesmo nome em níveis diferentes
x = 1  # Variável no escopo global

def escopo_externo():
    x = 10  # Variável local da função 'escopo_externo'
    
    def escopo_interno():
        y = 2  # Variável local da função 'escopo_interno'
        print("Função interna (x e y):", x, y)  # Acessa x=10 
        # (do escopo externo) e y=2 (local)
    
    escopo_interno()
    print("Função externa (x):", x)  # Acessa x=10

print("Fora da função (x):", x)  # Acessa x=1 (global)
escopo_externo()
print("Fora da função novamente (x):", x)  # Continua x=1 (não foi alterado)

print("Exemplo 3 - Escopos aninhados com mesmo nome ----------------------")