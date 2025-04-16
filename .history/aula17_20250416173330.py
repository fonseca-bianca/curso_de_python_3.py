#CONDICIONAIS
#cód irá checar condição True, se NÃO for, ele vai ler outro 'if' no cód
# até encontrar um cond True e sair do bloco

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print("Código pra condição 1")
elif condicao2:    
    print("Código pra condição 2")
elif condicao3:
    print("Código pra condição 3")
elif condicao4:
    print("Código pra condição 4")
else:
    print("Nenhuma condição satisfeita")

if 10 == 10:
    print("Esse é outro bloco 'if'")
    
