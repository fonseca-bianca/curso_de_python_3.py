"""
Escopo de funções:
NÃO temos acesso a nomes de escopos internos nos escopos externos
GLOBAL: faz a variável do escopo externo ser a MESMA no escopo interno
essa palavra existe, MAS NÃO é boa prática usar (nem mesmo o cód como está 
escrito abaixo).
Cada variável 'x' abaixo é uma variável diferente, pois cada uma está num escopo
diferente.
"""

x = 1

def escopo_externo():
    #global x
    # x = 10
    y = 20
    
    def escopo_interno():
        #global x
        # x = 11
        y = 2
        print(x, y)
    print(y)
        
    escopo_interno()
    #print(x)
    
    
#print(x)
escopo_externo()
#print(x)

""" 
OBS.: VAI PULAR DE DENTRO PRA FORA PRA ENCONTRAR UM 'X' VÁLIDO, NUNCA o contrário
conforme está acima comentado o cód, vai ser impresso: 1 2
porque, o 'x' q será lido será o q está disponível, no caso, o do escopo externo
"""