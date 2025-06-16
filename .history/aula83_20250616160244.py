"""
Empacotamento e desempacotamento de Dicionários + *args e **kwargs

✅ Dica rápida:
* → tupla de valores.

** → dicionário de pares chave=valor.
___________________________________________________________________________
- Empacotamento:
    É quando usamos * ou ** na definição da função pra agrupar argumentos
        ex.:
            def funcao(*args, **kwargs):
            pass

- Desempacotamento:
    É quando usamos * ou ** na chamada da função para espalhar os dados   
        ex.:
            def saudacao(nome, idade):
                print(f"Olá {nome}, {idade} anos")

            dados = {'nome': 'Bianca', 'idade': 30}
            saudacao(**dados)  # Desempacota o dicionário em nome e idade 
    
- **kwargs: keyword arguments (argumentos nomeados)
    Recebe vários argumentos nomeados (chave=valor) em forma de dicionário

- *args (argumentos posicionais):
    Recebe vários valores posicionais em forma de tupla.
"""

a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items() OU pessoa.values()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# extração dos dados do dicionário usando desempacotamento **
pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#                           key = value , key = value
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)