""" 
Funções em Python (def)
são trechos de cód usadas pra replicar/reutilizar determinada ação ao longo 
do cód.
Podem receber valores como parâmetros (argumentos) e podem retornar valores 
específicos.
padrão: None (retornam Nada), NÃO valor, como se fosse um 'vazio' (falsy)
"""

# Definindo uma função com parâmetros:
    #  precisa passar valores correspondentes (argumentos) ao chamá-la
    
def imprimir(a, b, c): # com parâmetros
    print("várias1")
    print("várias2")
    print("várias3")

imprimir(1, 2, 3) # com argumentos (valores) dos parâmetros
imprimir(1,)

# print("------------------------------------------------")
# Definindo uma função com parâmetros opcionais:
    # se quiser deixar os parâmetros opcionais, você pode definir valores padrão, 
    # assim:

# def imprimir(a=1, b=2, c=3):
#     print(a, b, c)

# print("------------------------------------------------")
# Definindo uma função sem parâmetros:
    # não precisa (nem pode) passar argumentos na chamada
    
# def imprimir( ): # sem parâmetros 
#     print("várias1")
#     print("várias2")
#     print("várias3")

# imprimir( ) # sem definição de parâmetros