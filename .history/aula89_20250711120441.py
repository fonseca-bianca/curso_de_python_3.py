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
"""
# Função dir():
print(dir("Ana")) 

# Função hasattr():
hasattr("Ana", "upper")  # True
hasattr("Ana", "voar")   # False

# Função getattr():
getattr("Ana", "upper")()  # chama "Ana".upper() → resultado: "ANA"