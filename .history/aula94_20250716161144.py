""" 
try, except, else e finally em Python:
    - Finally:
        SEMPRE será executado, mesmo q ocorra ou não um erro
"""
try:
    print(123)
    x = 10/0
    
finally:
    print("Executou o 'try' e o 'finally'")