"""
Problema dos parâmetros mutáveis em funções Python:
- shallow copy, deep copy, copy, coisas mutáveis

    * NÃO usar parâmetros mutáveis no lugar dos parâmetros de valor padrão de 
    uma função
        ex.:
            def func(a, b=[]): # NÃO FAÇA ISSO
            - SOLUÇÃO:
                def func(a, b=None): # 'b' passa a ser Imutável
                    if b is None:
                        b = []
                        
                        ** já q o corpo da função é executado toda vez q a 
                        função é chamada, por isso é necessário criar a lista
                        dentro da função, pra garantir q toda vez q a função
                        for chamada, uma nova lista vazia será criada.
"""

def adc_client(name, client=None):
    if client is None:
        client = []
    client.append(name)
    return client

# são listas independentes
client1 = []
generated_client1= adc_client('Luiz', client1)
adc_client('Joana', client1)
print(generated_client1)
# ['Luiz', 'Joana']

generated_client2 = adc_client('Helena') # client2 = None, por isso foi criada
# uma nova lista vazia dentro da função com base na lógica da função 'adc_client'
adc_client('Maria', generated_client2)
print(generated_client2)
# ['Helena', 'Maria']