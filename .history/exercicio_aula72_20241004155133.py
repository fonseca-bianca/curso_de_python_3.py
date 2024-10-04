"""
EXERCÍCIO EM FUNÇÕES
Crie uma função que multiplica todos os argumentos NÃO nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
Crie uma função que fale se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
import math

def multiplies_all(*args): #*args: passando qtde qlqr de args NÃO nomeados pra função
    return math.prod(args) # math.prod(args): calcula o produto de todos os valores passados na função

result = multiplies_all(1, 2, 3, 4, 5, 6, 7) # var 'resultado' armazena produto total

print(f"O resultado da multiplicação é: {result}") # total 5040

def even_or_odd(result):
    if result % 2 == 0:
        return f"O resultado {result} é par"
    # else: (se tivesse o else, o 'return' teria q estar dentro do else)
    return f"O resultado {result} é ímpar."

# retorno da função 'par_ou_impar' armazenado na variável 'retorno_par_ou_impar'
return_even_or_odd = even_or_odd(result)
print(return_even_or_odd)

""" 
OU a função par_ou_impar poderia ser escrita com o 'print' ao invés do 'return', assim:
def par_ou_impar(resultado):
    if resultado % 2 == 0:
        print(f"O resultado {resultado} é par")
    else:
        print(f"O resultado {resultado} é ímpar.")

par_ou_impar(resultado)
"""