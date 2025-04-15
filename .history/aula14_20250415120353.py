"""
OBS.: se colocar os nomes das variáveis nas chaves, então vc irá ficar 
'refém' de colocar, no .format() na MESMA ordem em q as variáveis estão na 
string.
* se colocar os índices das variáveis entre chaves, então vc pode colocar
os nomes das variáveis na ordem que quiser no .format()
"""

a = "AAA"
b = "BBB"
c = 1.1
string = 'b={0} a={nome1} c={nome2:.2f}' #'b' está na posição ZERO, pois é o 
# índice correspondente na ordem das strings
formato = string.format(
    b, nome2=c, nome1=a
)
# Parâmetro nomeado: 
# é dado nome às coisas dentro da chamada/criação da função
# OBS.: se o 1º parâmetro for nomeado, os outros também devem ser nomeados,
# bem como deverão seguir a ordem em que foram definidos na função
# se o 1º NÃO for, então os outros podem ou não serem nomeados
print(formato)