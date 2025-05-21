"""
Escopo de funções:
NÃO temos acesso a nomes de escopos internos nos escopos externos
GLOBAL: faz a variável do escopo externo ser a MESMA no escopo interno
essa palavra existe, MAS NÃO é boa prática usar (nem mesmo o cód como está 
escrito abaixo).
Cada variável 'x' abaixo é uma variável diferente, pois cada uma está num 
escopo diferente.
--> Quando fizer debugger, verificar CALL STACK (o local na memória onde são
alocadas as variáveis conforme cada escopo)
"""

x = 1

def escopo_externo():
    # global x
    # x = 10
    y = 20
    
    def escopo_interno():
        # global x
        # x = 11
        y = 2
        print(x, y)
    print(y)
        
    escopo_interno()
    #print(x)
    
    
#print(x)
escopo_externo()
#print(x)

# OBS.: 
#   VAI PULAR DE DENTRO PRA FORA PRA ENCONTRAR UM 'X' VÁLIDO, NUNCA o contrário
# conforme está acima comentado o cód, vai ser impresso: 1 2
