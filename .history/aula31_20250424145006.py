"""
* Flag:
    - uma flag é uma variável que serve para indicar se uma condição foi atendida ou
    não.
    - ela pode ser utilizada para controlar o fluxo de execução do programa
    - marca um local no código onde uma condição foi atendida ou não.

*None:
    - é um NÃO valor

* is e is not:
    - é ou NÃO é (tipo, valor, identidade)

* id:
    - identifica o endereço de um objeto na memória (identidade)	

IDENTIDADE DO VALOR Q ESTÁ NA MEMÓRIA:
Se colocarmos o MESMO valor em variáveis diferentes, o Python vai interpretar 
como valores literais e, portanto, iguais, logo, ambas as variáveis diferentes
terão o MESMO endereço na Memória

v1 = "a"
v2 = "a"
print(id(v1)) # 4334936816
print(id(v2)) # 4334936816
"""

condicao = False
passou_no_if = None # condição declarada FORA do bloco pra poder usá-la DENTRO
# do bloco

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça nada")
    
if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")