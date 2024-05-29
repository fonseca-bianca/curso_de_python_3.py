nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

# nome é o primeiro argumento, o qual corresponde ao índice {0}.
# idade é o segundo argumento, o qual corresponde ao índice {1}.
# porém, na variável 'formato' declaramos os índices em outra ordem q NÃO a crescente, por isso NÃO está na ordem 'nome... idade...'
# 'formato' é variável do tipo string. Em Python, quando uma string é atribuída à variável, ela se torna uma string