""" formatação de String:
* pra não precisar colocar um monte de vírgulas ou concatenações pra escrever 
uma frase
* utiliza-se variáveis dentro da f-string envolvidas por chaves {}
"""
nome_completo = "Bianca Fonseca"
peso = 52
altura = 1.52
imc = peso / (altura * altura)
#print(nome_completo, "tem", altura, "altura, pesa", peso, "quilos e seu IMC 
# é", imc)

# abaixo, toda a expressão está entre parêntes pro interpretador entender tudo
# como uma string só, conforme PEP 8
linha_1 = (
        f'{nome_completo} tem {altura:.2f} metros de altura,'
        f' pesa {peso} quilos e seu IMC é {imc:.2f}.'
)
print(linha_1)

#____:.2f --> quer dizer que queremos q apareça 2 casas depois do ponto

dinheiro = 1.52
linha_2 = f'o valor em real (moeda) é de R$ {dinheiro:.2f}'
print(linha_2)