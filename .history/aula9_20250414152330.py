adicao = 10.2 + 10
print('adição:', adicao)

divisao = 10 / 3
print('divisão:', divisao)

divisao_inteira = 10 // 3.0
print('divisão inteira:', divisao_inteira)
# nessa categoria, a divisão inteira é o mesmo que o floor division, ou seja, 
# o resultado é arredondado para baixo e colocado um zero após o ponto (quando
# se tratar de float)

exponenciacao = 2 ** 10
print('exponenciação/potenciação:', exponenciacao)

modulo = 55 % 2 # resto da divisão
print('módulo:', modulo)

# o Módulo ajuda a identificar se um número é divisível por outro. Se o resto
# der ZERO, então o número é divisível pelo outro, se der 1, então não é.
print(10 % 8 == 0) # False