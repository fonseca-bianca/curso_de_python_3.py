"""
Escopo de funções:
NÃO temos acesso a nomes de escopos internos nos escopos externos

GLOBAL: 
faz a variável do escopo externo ser a MESMA no escopo interno
essa palavra existe, MAS NÃO é boa prática usar o nome 'global' pra variável
(nem mesmo o cód como está escrito abaixo).

Cada variável 'x' abaixo é uma variável diferente, pois cada uma está num 
escopo diferente.
OBS.:
    Quando fizer debugger, verificar CALL STACK (o local na memória onde são
alocadas as variáveis conforme cada escopo)

CALL STACK: é a pilha de chamadas, onde cada função chamada é empilhada
e, quando termina, é desempilhada.
- OBS.:
    VAI PULAR DE DENTRO PRA FORA PRA ENCONTRAR UM 'X' VÁLIDO, NUNCA o contrário
- está no VS Code quando selecionamos o Debugger
- clica no Debugger (seleciona a parte do cód q tu quer ver) e depois
olha a CALL STACK q vai aparecer na parte de baixo o <module> onde está o
cód
"""

x = 1

def escopo_externo():
    # global x
    x = 10
    # y = 20
    
    def escopo_interno():
        # global x
        x = 11
        y = 20
        print(x, y)
    print(x)
        
    escopo_interno()
    # print(x)
    
    
print(x) # vai imprimir 1 (var global)
escopo_externo() # Vai imprimir 10 (x local de escopo_externo) e depois 11 20
# (x e y locais de escopo_interno)
print(x) # vai imprimir 1 (var global)

"""
OBS.:
Quando o programa chama a função escopo_externo(), a execução é desviada 
para essa função. A linguagem Python usa a Call Stack para controlar essas 
chamadas: um novo frame é empilhado na memória, com espaço próprio para as 
variáveis locais dessa função.
Nesse caso, ao chamar escopo_externo(), será criada uma var local x = 10
Dentro dela, ao chamar escopo_interno(), outro frame é adicionado à pilha, 
com suas próprias variáveis locais (x = 11 e y = 20).
Ao final de cada função, seu frame é removido da Call Stack, e o programa 
retorna para o ponto onde a função foi chamada.
"""

# OBS.: 
#   VAI PULAR DE DENTRO PRA FORA PRA ENCONTRAR UM 'X' VÁLIDO, NUNCA o contrário
# conforme está acima comentado o cód, vai ser impresso: 1 2
