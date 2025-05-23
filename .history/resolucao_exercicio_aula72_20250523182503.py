"""
EXERCÍCIO EM FUNÇÕES
Crie uma função que multiplica todos os argumentos NÃO nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
Crie uma função que fale se o número é par ou ímpar.
Retorne se o número é par ou ímpar.

** cód feito pelo prof. pra resolver o problema **
"""

def multiplicar(*args):
    total = 1 # NÃO colocar zero, pq qlqr nº x 0 é 0
    for numero in args:
        total *= numero
    return total


# pode acentuação, porém, NÃO é recomendado
multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)
print(10*2*3*4*5) # confere q os números passados acima resultam em 1200


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_ou_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_ou_impar = par_ou_impar
dois_e_par = outro_par_ou_impar(2)
print(dois_e_par)
print(par_ou_impar(3))
print(par_ou_impar(15))
print(par_ou_impar(16))

print(par_ou_impar is outro_par_ou_impar)
