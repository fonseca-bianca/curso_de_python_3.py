"""
CUIDADO com os tipos de Dados Mutáveis: list e copy
uso sinal = : copiando o valor (Imutável)
uso sinal = : aponta pro mesmo valor na memória (Mutável)

- Para tipos **IMUTÁVEIS** (str, int, float, tuple, etc.):
  - Uso do sinal `=` copia o **valor**, e alterações em uma variável não 
  afetam a outra.
  
- Para tipos **MUTÁVEIS** (list, dict, set, etc.):
  - Uso do sinal `=` faz ambas as variáveis **apontarem para o mesmo objeto 
  na memória**.
  - Modificações em uma afetam a outra.
  
- Para copiar **mutáveis** de forma independente, use `.copy()`
ou `list(original)`
"""
nome1 = "Ana"
outra_variavel = nome1 # Cria uma NOVA 'cópia' do valor (pois str é imutável)
nome1 = "João" # Atribui um novo valor a `nome1`, sem afetar `outra_variavel`
print(nome1) # João. Tem um id na memória do programa 
print(outra_variavel) # Ana. Tem outro id na memória do programa


# uso sinal = : aponta pro mesmo valor na memória (Mutável)
lista_a = ["João", "Maria"]
lista_b = lista_a 

lista_a[0] = "Mexe na lista_a e altera o mesmo valor na lista_b" 
# pq ambas apontam pro mesmo valor na memória"
print(lista_b)

# utilizando método 'copy':
lista_a = ["João", "Maria", "Tyrion"]
lista_b = lista_a.copy() # retornar os valores da 'lista_a' pra 'lista_b' 

lista_a[0] = "Missandre" # pq ambas apontam pro mesmo valor na memória"
print(lista_a) # output: ['Missandre', 'Maria', 'Tyrion']
print(lista_b) # imprime 'lista_b' com efeito do método 'copy', isto é, o
# .copy() foi chamado ANTES da alteração no índice zero da lista_a
#                output: ["João", "Maria", "Tyrion"]