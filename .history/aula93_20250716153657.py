"""
Tratamento de exceções em Python:
Try, except, else e finally
 - Except:
    OBS.: 
        são Classes em Python q representam erros.
        Normalmente vemos qual o erro q aparece e tratamos ele especificamente
        PORÉM, caso não seja possível ou seja um cód pronto de terceiro, 
        é possível tratar os erros com uma classe genérica 'Exception', mas
        não é muito recomendado, pq não saberemos qual erro está sendo tratado.
    informar QUAL o erro está sendo tratado
        ANTES do erro vai aparecer o nome da Exceção q está ocorrendo
            ex.:
            nome da exceção  :      erro
            ZeroDivisionError: division by zero
            (é uma classe)
    pode ter mais de um except tratando diferentes erros
"""
try:
    x = 1 / 0
except ZeroDivisionError: 
    print("Divisão por zero não é permitida.")
else:
    print("Divisão realizada com sucesso.")
finally:
    print("Bloco 'finally' é sempre executado, havendo erro ou não.")

