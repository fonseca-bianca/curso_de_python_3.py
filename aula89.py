"""
No Debugger, vai na aba 'Debug Console' e digita:
    dir(), hasattr() ou getattr()
           has a ttr    get a ttr
Ou no próprio código
Pra chegar se o método existe dentro de determinado objeto qualquer

Função:	        Serve para:	                                Retorna:
dir()	        Ver tudo que o objeto tem:	                lista
                atributos, métodos
hasattr()	    Ver se algo existe no objeto:	            bool
                tem aquele atributo/método específico
getattr()	    Pegar e usar algo do objeto pelo nome:	    valor
                pega o valor de um atributo (ou método) do objeto por nome
"""
# Função dir():
print(dir("Ana")) 

# Função hasattr():
print(hasattr("Ana", "upper"))  # True
print(hasattr("Ana", "voar"))   # False

# Função getattr():
print(getattr("Ana", "upper")())  # chama "Ana".upper() → resultado: "ANA"