"""
O 'for' por 'baixo dos panos'
* iterável: str, range, etc . Método dentro do iterável em Python: .__iter__() --> 
retorna um 'iterador' (q é OUTRO Objeto q vai saber entregar um elemento por vez da string)
.__iter__() --> pode usar iter() q é mais fácil
* iterador: sabe entregar um valor por vez
* next (chamar dentro do 'iterator'): me entregue o próximo valor
* iter: me entrege o seu iterador
"""

#nome = "Luiz".__iter__()
nome = iter("Luiz")
print(next(nome))

