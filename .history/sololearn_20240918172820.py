# budget = 20
# print(budget + 10)

# price = 14
# discount = 0.2 * price
# final_price = price - discount
# print(final_price)

# items = 18
# boxes = 6
# print(items/boxes)

# start = 0
# end = 10
# while start < end:
#     start += 1
#     print(start)
    
# linhas = 2
# colunas = 2
 
# linha = 1
# while linha <= linhas:
#     coluna = 1
#     while coluna <= colunas:
#         print(linha, coluna)
#         coluna += 1
#     linha += 1
    
# score1 = int(input("Enter a score1: "))  
# score2 = int(input("Enter a score2: "))
# total_score = score1 + score2
# print(total_score)

# a = 14
# b = "km" --> gera erro, pois em Python NÃO é permitido concatenar string com int

# a = 14
# b = "km"
# print(str(a) + b) # tem q transformar o int em string, aí o Python consegue concatená-los
# print("14" + "km") # ou fazer a alteração do 14 para "14" direto no print


# cucumbers = 100
# num_people = 6
# whole_cucumbers_per_person = cucumbers / num_people
# print(whole_cucumbers_per_person)

# string_num = "7.5"
# print (float(string_num)) 


"""ambos vão imprimir a mesma coisa = 0 1 2 | 0 1 2
for i in range(3):
    print(i)
    
print("--")

for something in range(3):
    print(something)
"""

# seats = 500
# while True:
#     if seats > 0:
#         print(f"Assentos disponíveis: {seats}")
#         seats -= 1
#     else:
#         print("Os bilhetes terminaram e não há mais assentos disponíveis.")
#         break

# seats = 500
# while seats > 0:
#     print(f"Assentos disponíveis: {seats}")
#     seats -= 1

# counter = 0
# while counter < 4:
#     print(counter)
#     counter += 1

"""
for i in range(3):
    print(i < 1)
    # sendo i = 0:
        # 0 < 1 = True
    # sendo i = 1:
        # 1 < 1 = False
    # sendo i = 2:
        # 2 < 1 = False
"""

# for i in range(3):
#     print("First") # impresso 3 vzs
#     print("Second") # impresso 3 vzs

# for box in range(50):
#     print("Package A") # imprime 50 vzs
# print("Task complete") # imprime após completar 50 vzs, pois está fora do loop

parrot = "Norwegian Blue"
print(len(parrot)) 
