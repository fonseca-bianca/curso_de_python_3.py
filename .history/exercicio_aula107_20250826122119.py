"""
Exercício: unindo listas

Crie uma função zipper (zipper de roupas) e ela deverá unir duas listas em 
ordem.
Use todos os valores da menor lista.
    ex.:
        ['Salvador', 'Ubatuba', 'Belo Horizonte']
        ['BA', 'SP', 'MG', 'RJ']
        
        # output:
        [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

def zipper_1(cidade):
    def cidade(*args, **kwargs):
        retorno_cidade = ["Salvador", "Ubatuba", "Belo Horizonte"]
        return retorno_cidade.append(cidade(*args, **kwargs))
    return cidade

def zipper_2(estado):
    def estado(*args, **kwargs):
        retorno_estado = ["BA", "SP", "MG", "RJ"]
        return retorno_estado.append(estado(*args, **kwargs))
    return estado

@zipper_2
@zipper_1
def unir_listas(zipper_1, zipper_2):
   return list(zip(zipper_1, zipper_2))

print(unir_listas(zipper_1, zipper_2))