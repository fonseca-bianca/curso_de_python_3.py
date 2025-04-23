"""
Formatação básica de strings:
* Tipos:
    - s: string
    - d/i: inteiro (decimal)
    - f: float
    - x/X: hexadecimal (minúsculo/MAIÚSCULO)
    - %: porcentagem (ex: 0.25% = 0.0025)
    
* Precisão:
    - .<n>f: nº casas decimais (float)

* Alinhamento:
    - (><^)(width):
        >: alinhado à direita (padrão para números) --> considerando dezena, 
        centena, milhar, milhões
        <: alinhado à esquerda (padrão para strings) --> considerando a 
        margem de escrita (como no word do windows)
        ^: centralizado --> considerando a margem de escrita (como 
        no word do windows)
* Sinal:
    -> +: força sinal (mesmo pra positivos)
    -> -: sinal apenas para negativos (padrão)

* Preenchimento:
    - 0: preenche com zeros à esquerda (ex: 05d → 00042)

* Flags de conversão:
    - !r: repr()
    - !s: str() (padrão)
    - !a: ascii()

* Exemplo:
    0>-100,.1f:
        Este exemplo NÃO é válido, pois há uma contradição entre > e -
            Escolher qual dos dois sinais usar (padrão é >)
"""



print(f"{100.0002524: >10,.4f}") 
# output:  100.0003

# sinal de negativo (-):
print(f"{-100.0002524: >10,.4f}")
# output: -100.0003

# sinal de positivo (+):
print(f"{100.0002524: >+20,.4f}") # o sinal de positivo é o default, mas 
# se quiser q o Python mostre, aí tem q fazer nesse formato
# 20 é a quantidade de espaço q se quer colocar entre o número e as margens

# output: +100.0003

var_alphabet = "ABC"
print(f"{var_alphabet: <10})") 
# output: ABC       ) 
#   10 espaços ocupados no total, sendo 3 ocupados pela string 'ABC'
#   e 7 espaços em branco à direita (<)
print(f"{var_alphabet: >10})")