a = "AAA"
b = "BBB"
c = 1.1
string = 'b={0} a={nome1} c={nome2:.2f}' #'b' está na posição ZERO, pois é o 
# índice correspondente na ordem das strings
formato = string.format(
    b, nome1=a, nome2=c
)
print(formato)