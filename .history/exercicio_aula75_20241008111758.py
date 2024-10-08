""" 
Exercício:
Crie funções que duplicam, triplicam e quadruplicam o número recebido
como parâmetro.
"""

def criar_multiplicador(multiplicador): # função-MÃE recebe 'multiplicador' como parâmetro
    def multiplicar(numero): #função-FILHA recebe 'numero' como parâmetro
        return numero * multiplicador # parâmetro da função-FILHA sendo multiplicado pelo parâmetro da função-MÃE recebe 'numero' como parâmetro
    return multiplicar 

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))  # Output: 10
print(triplicar(5))  # Output: 15
print(quadruplicar(5))  # Output: 20