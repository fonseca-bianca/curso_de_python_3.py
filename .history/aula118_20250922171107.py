"""
Problema dos parâmetros mutáveis em funções Python:
- shallow copy, deep copy, copy, coisas mutáveis

    * NÃO usar parâmetros mutáveis no lugar dos parâmetros de valor padrão de 
    uma função
        ex.:
            def func(a, b=[]): # NÃO FAÇA ISSO
            - SOLUÇÃO:
                def func(a, b=None):
                    if b is None:
                        b = []
"""
