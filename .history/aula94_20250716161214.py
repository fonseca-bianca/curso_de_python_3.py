""" 
try, except, else e finally em Python:
    - Finally:
        SEMPRE será executado, mesmo q ocorra ou não um erro
"""
try:
    print(123)
    x = 10/0
except ZeroDivisionError:
    print("Não pode dividir por zero")
finally:
    print("Executou o 'try' e o 'finally'")