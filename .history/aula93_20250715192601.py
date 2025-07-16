"""
Try, except, else e finally:
tratamento de exceções em Python
"""
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida.")
else:
    print("Divisão realizada com sucesso.")
finally:
    print("Bloco 'finally' é sempre executado, havendo erro ou não")

