"""
Closure e funções que retornam outras funções
"""

def saudacao_generica(saudar):
    def saudar_pessoa(nome):
        return f"{saudar}, {nome}!"
    return saudar_pessoa