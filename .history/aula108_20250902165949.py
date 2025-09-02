"""
count(): 
    conta quantas vezes um elemento aparece em uma lista
    NÃO é nativo do Python
    
    * range(): NÃO é um iterator
    
    Range          |           Count
    -------------- | ----------------
    __iter__       | __len__
    __next__       | __getitem__
    melhor qndo    | continua gerando 
    sabemos número | números até ser 
    de iterações,  | explicitamente 
    pq ele tem um  | interrompido por
    limite         | um 'break'
    
    OBS.:
      se chamarmos o 'iter' do iterator, ele chama o próprio iterator
"""