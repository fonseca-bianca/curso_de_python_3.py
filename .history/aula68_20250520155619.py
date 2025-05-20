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

# aq a variável é definida FORA da função, como se fosse um 'vizinho' da 
# função, ou seja, é possível a variável do escopo global (acima), mas NÃO
# pode acessar variáveis do escopo local (abaixo)

x = 1
# ficaria assim:
# def escopo():
#     print(x)

# escopo()    



# aq a função é apenas definida
def escopo():
    z = 1
    print(z) # 'z' está DENTRO da função

# aq a função é chamada de fato:
# ou seja, o cód é executado de baixo pra cima, só quando a função é chamada
# é q o cód é executado
escopo()

print("----------------------------------------------------------------")

a = 5 # escopo global

def funcao_escopo_maior():
    def funcao_escopo_menor():
        b = 10 # escopo local, acessada somente na funcao_escopo_menor()
        print(a, b)
        
    funcao_escopo_menor()
    print(a)
    
funcao_escopo_maior()

# OBS.: o q está no escopo da funcao_escopo_menor() NÃO é lido pela 
# funcao_escopo_maior()


print("----------------------------------------------------------------")

x = 1 # 1º valor a ser impresso (escopo global)

def escopo_maior():
    x = 10
    
    def escopo_menor():
        y = 2
        print(x, y) # 2° valor a ser impresso. 'x' aq é o "x = 10" do 
        # escopo maior
        
    escopo_menor()
    print(x) # 3° valor a ser impresso. Vai imprimir '10', que é o "x" local 
    # da função 'escopo_maior'
    
print(x) # vai imprimir 1, pois o valor da variável do escopo_maior()
escopo_maior() # vai imprimir 10, pois o valor da variável do escopo_maior()
print(x) # vai imprimir 1 novamente, pois o valor da variável do 
# escopo_maior(). O valor de 'x' no escopo global não foi alterado pela 
# função 'escopo_maior'