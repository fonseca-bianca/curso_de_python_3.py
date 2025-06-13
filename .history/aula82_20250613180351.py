"""
Funções Lambda Complexas:
    Múltiplos argumentos;
    Mais de uma operação dentro da expressão;
    Ou que retorna tuplas, dicionários, listas, expressões condicionais, 
    chamadas de função, etc.;
    lambda não pode ter múltiplas linhas (sem if/else completo, for, while 
    ou print separados);
    Ideal para uso rápido e simples, mas se ficar muito complexa, é melhor 
    usar def.;
    Usar em funções como map(), filter(), sorted(), reduce();
    usar quando a lógica é curta e clara.
    
    ex.: Lambda usada pra ordenar Nome Completo:
        sorted(lista, key=lambda x: x['nome'] + ' ' + x['sobrenome'])

Estrutura Lambda:
    lambda argumentos: expressão
"""

def executa(funcao, *args):
    return funcao(*args)
# Recebe uma função (funcao) e qualquer quantidade de argumentos (*args).
# Usa funcao(*args) pra executar essa função com os argumentos recebidos.
# 💡 *args significa: "junte todos os argumentos extras em uma tupla".


# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


# duplica = cria_multiplicador(2)

# Primeiro uso: função lambda aninhada (função que retorna outra função)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2)) # duplica(2) => 2 * 2 = 4
# lambda m: lambda n: n * m --> cria uma função que retorna outra função.
# Você passa 2 como argumento (m = 2), então vira: lambda n: n * 2
# Isso é igual a uma função "multiplicador" que duplica o valor.



print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)