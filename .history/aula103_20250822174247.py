"""
Funções Decoradoras e Decoradores no Python:
Decorar = adicionar/remover/restringir/alterar
* Funções Decoradoras:
    são funções que decoram outras funções, como o caso do Closure
** Decoradores:
    usados pra fazer o Python usar as funções decoradoras em outras funções
    modificam comportamento de uma função dinamicamente
    a. baseados em Funções:
       função q recebe um objeto de função como argumento e retorna OUTRO obj
de função com funcionalidade estendida (fechamento)
       necessário usar Closure 
    b. baseados em Classes:
"""

print("Decorador baseado em Função:")
def decorator(function): # função externa
    def closure(): # função interna
        print("Doing something before calling the Function")
        function()
        print("Doing something after calling the Function")
    return closure