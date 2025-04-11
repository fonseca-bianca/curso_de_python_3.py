"""
* Conversão de tipos = coerção, type convertion, typecasting, coercion:
converte um tipo em outro

*EXCETO:
    str, int, float, bool = são tipos primitivos Imutáveis
"""

#coloca na frente o tipo que se quer converter 
print(int("1") + int(1.0)) #converte o primeiro q é 'str' e o segundo q é 
#'float'
print(float("1") + float(1)) 
print(10 == 10) #comparação de igualdade. Ambos são 'int'
print(type(10 == 10))