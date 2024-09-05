"""While/else"""
# em Python, o while tem else
# quando o laço while é executado por completo, aí o laço else será executado
# OBS.: se der um 'break' no while, o else NÃO será executado

string = "Valor qualquer"

i = 0
while i < len(string):
    letra = string[i]
    
    print(letra)
    i += 1
else:
    print("O else foi executado")

print("Fora do bloco 'while'")