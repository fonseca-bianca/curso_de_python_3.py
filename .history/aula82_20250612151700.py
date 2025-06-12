"""
Funções Lambda Complexas:
    Múltiplos argumentos;
    Mais de uma operação dentro da expressão;
    Ou que retorna tuplas, dicionários, listas, expressões condicionais, 
    chamadas de função, etc.;
    lambda não pode ter múltiplas linhas (sem if/else completo, for, while 
    ou print separados);
    Ideal para uso rápido e simples, mas se ficar muito complexa, é melhor 
    usar def.;
    Usar em funções como map(), filter(), sorted(), reduce();
    usar quando a lógica é curta e clara.
    
    ex.: Lambda usada pra ordenar Nome Completo:
        sorted(lista, key=lambda x: x['nome'] + ' ' + x['sobrenome'])

Estrutura Lambda:
    lambda argumentos: expressão
"""