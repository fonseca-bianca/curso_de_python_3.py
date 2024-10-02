"""
Escopo de funções:
NÃO temos acesso a nomes de escopos internos nos escopos externos
GLOBAL: faz a variável do escopo externo ser a MESMA no escopo interno
"""

x = 1

def escopo_externo():
    #global x
    # x = 10
    
    def escopo_interno():
        #global x
        # x = 11
        y = 2
        print(x, y)
        
    escopo_interno()
    #print(x)
    
    
#print(x)
escopo_externo()
#print(x)

""" 
conforme está acima comentado o cód, vai ser impresso: 1 2
porque, o 'x' q será lido será o q está disponível, no caso, o do escopo externo
"""