import time

start_time = time.time()  # Armazena o tempo inicial
duration = 60  # Duração em segundos (1 minuto)
count = 0  # Contador de impressões

while (time.time() - start_time) < duration:
    print(1)
    count += 1

print(f"O valor foi {count}")