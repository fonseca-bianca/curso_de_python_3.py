import statistics

comprimento = [17,12,9,23,14,6,3,18,42,25,18,12,34,5,17,20,7,8,21,13,31,24,9]
minimo = min(comprimento)
maximo = max(comprimento)
mediana = statistics.median(comprimento)

print(minimo)
print(maximo)
print(mediana)