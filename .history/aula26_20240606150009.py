#sinais:

print(f"{100.0002524: >10,.4f}")
#sinal de negativo (-):
print(f"{-100.0002524: >10,.4f}")
#sinal de positivo (+):
print(f"{100.0002524: >+20,.4f}") #o sinal de positivo é o default, mas se quiser q o Python mostre, aí tem q fazer nesse formato
#20 é a quantidade de espaço q se quer colocar entre o número e as margens
#> (Esquerda), < (Direita), ^ (Centro)