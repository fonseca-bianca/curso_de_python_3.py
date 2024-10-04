"""
EXERCÍCIO EM FUNÇÕES
Crie uma função que multiplica todos os argumentos NÃO nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
Crie uma função que fale se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
import math

def multiplica_todos(*args): #*args: passando qtde qlqr de args NÃO nomeados pra função
    return math.prod(args) # math.prod(args): calcula o produto de todos os valores passados na função

    def par_ou_impar(resultado):
        if resultado % 2 == 0:
            print(f"O resultado {resultado} é par")
        else:
            print(f"O resultado {resultado} é ímpar.")

resultado = multiplica_todos(1, 2, 3, 4, 5, 6, 7) # var 'resultado' armazena produto total

print(resultado) # total 5040


