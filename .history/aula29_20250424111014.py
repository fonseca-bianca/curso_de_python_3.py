numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")   
except:
    print("O valor digitado não é um número")

# if numero_str.isdigit(): --> .isdigit() SÓ aceita números inteiros
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2}")
# else:
#     print("O valor digitado não é um número")
    