nome_completo = "Bianca Fonseca"
peso = 52
altura = 1.52
imc = peso / (altura * altura)
print(nome_completo, "tem", altura, "altura, pesa", peso, 
      f"quilos e seu IMC é {imc:.2f}")

""" 
Ellipsis: ...
* usado como placeholder (marcador de código ainda não implementado):
- como "ainda vou escrever isso aqui"
* Em bibliotecas que lidam com arrays, como NumPy:
- array = np.ones((3, 4, 5))
print(array[..., 0])  # Acessa todos os primeiros elementos da última dimensão
"""
print(type(...))
