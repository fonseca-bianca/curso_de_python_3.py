# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    # 'as' (aliase, "apelido"): é usado para dar um nome à exceção
    # 'e' é o nome da exceção
    
    print(e.__class__.__name__) #
    print(e)
except NameError:
    print('Nome b não está definido')
    # coloca os nomes das exceções quando vc JÁ SABE quais são os erros
except (TypeError, IndexError) as error: # 'error' é o nome da exceção.
    # trata MAIS de um erro (TypeError e IndexError)
    print('TypeError + IndexError') # trata ambos os erros
    
    print('Nome:', error.__class__.__name__) 
    # error: é a instância da classe
    # __class__: é um Atributo q retorna a classe do objeto
    # __name__: é um Atributo q retorna o nome da classe
except Exception: # classe genérica para tratar exceções
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')