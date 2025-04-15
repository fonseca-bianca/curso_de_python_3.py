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
    b, nome1=a, nome2=c
)
print(formato)