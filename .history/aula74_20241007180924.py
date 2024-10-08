"""
Closure e funções que retornam outras funções
"""
def outer():
    a = 25
    name = "python"
    
    def inner(prefix):
        print(prefix, name)
        
    return inner

print(outer())