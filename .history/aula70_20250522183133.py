"""
Retorno de valores das funções (return).
SOMENTE de dentro da função, pq só função tem essa palavra
O retorno desses valores poderá ser utilizado no cód, seja em variáveis ou
outras partes do cód

print(): 
    é uma função que só EXIBE coisas, valores na tela (saída do sistema)
    mostra informações no console pro programador, geralmente pra depuração
    ou verificação de valores
    Não interage com o sistema nem altera a lógica do programa, apenas exibe 
    dados
    NÃO tem valor (é None)
    * é como se fosse o 'console.log' do JavaScript
"""

def soma(x, y):
    return x + y
    # print(1 + 1) --> Code is unreachable (inalcançável após o 'return')

soma1 = soma(1, 1) # retorna Literal[2]
soma2 = soma(2, 2) # retorna Literal[4]

print(soma1 + soma2) 

# o código irá retornar a soma das duas variáveis soma1 e soma2, pq tem o 
# 'return' acima somando os valores de 'x' e 'y' 


def olha_so(c, d):
    print("Olha")
    print("só")
    print("que")
    print("legal")
    
    if c > 10:
        return 10
    return c + d 
    # aq ´é como se fosse o 'else', mas NÃO precisa especificar, 
    # pq se a outra condição for FALSE, então o 2º return será 
    # lido
    
    

olha1 = olha_so(2, 2)
olha2 = olha_so(3, 3)

print(olha1 + olha2) 


# Porque o código retorna "Olha só que legal" 2 vezes?
# Seria porque a frase "Olha só que legal" estaria nos lugares de 'x' e 'y'
# da função def soma???

# Retorno do código:
# Olha
# só
# que
# legal
# Olha
# só
# que
# legal
# 6

# --> O fluxo de execução é o seguinte:

#     Chama soma(1, 1): imprime "Olha", "só", "que", "legal", e 
# depois retorna 2.
#     Chama soma(2, 2): imprime "Olha", "só", "que", "legal", e 
# depois retorna 4.
#     Soma os resultados retornados (2 + 4 = 6) e imprime 6.


# def diminui(a, b): 
#     ...
#  essa função retorna None, pq não foi especificado o q ela deve retornar


# def somatorio(x, y):
#     print(x + y)
    
# somatorio1 = somatorio(1, 1)
# somatorio2 = somatorio(2, 2)

# print(somatorio1 + somatorio2) 

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
#   a função somatorio não retorna nada, mas precisamos que ela retorne 
# (uso do 'return') algo justamente pra saber o q fazer com o retorno 
# dela (somar, subtrair etc.)