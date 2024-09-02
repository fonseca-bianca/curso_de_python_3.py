from datetime import datetime
import random

# Lista para armazenar os times
times = []

# Adiciona 8 times com atributos fictícios (substitua pelos dados reais)
for i in range(1, 9):
    time = {
        'nome': f'Time {i}',  # Substitua pelos dados reais
        'gritoGuerra': f'Grito {i}',  # Substitua pelos dados reais
        'anoFundacao': f'Ano {i}'  # Substitua pelos dados reais
    }
    times.append(time)

print("Lista de times:", times)

# Função para sortear um time aleatoriamente e removê-lo da lista
def sortear_time(times_list):
    if not times_list:
        return None
    random_index = random.randrange(len(times_list))
    return times_list.pop(random_index)

# Sorteia e remove 8 times da lista
time1 = sortear_time(times)
print("Time sorteado:", time1)
print("Times restantes:", times)

time2 = sortear_time(times)
print("Time sorteado:", time2)
print("Times restantes:", times)

time3 = sortear_time(times)
print("Time sorteado:", time3)
print("Times restantes:", times)

time4 = sortear_time(times)
print("Time sorteado:", time4)
print("Times restantes:", times)

time5 = sortear_time(times)
print("Time sorteado:", time5)
print("Times restantes:", times)

time6 = sortear_time(times)
print("Time sorteado:", time6)
print("Times restantes:", times)

time7 = sortear_time(times)
print("Time sorteado:", time7)
print("Times restantes:", times)

time8 = sortear_time(times)
print("Time sorteado:", time8)
print("Times restantes:", times)

#class TimesQuadribol:
#    def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
#        self.nome = nome
#        self.grito_de_guerra = grito_de_guerra
#        self.ano_de_fundacao = ano_de_fundacao
#
#    def mostrar_informacoes_times(self):
#        print(f"Nome do time: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}")
#
#def inserir_dados():
#    times = []
#    for i in range(1, ):
#        while True:
#            try:
#                nome = input(f"Qual o nome do time {i}? ")
#                if len(nome) <= 10:
#                    print(f"O nome do time {i} é: {nome}")
#                    break
#                raise Exception
#            except Exception:
#                print("O nome do time precisa ter, no máximo, 10 caracteres.")
#        
#        while True:
#            try:
#                grito_de_guerra = input(f"Qual o grito de guerra do time {i}? ")
#                if len(grito_de_guerra) <= 20:
#                    print(f"O grito de guerra do time {i} é: {grito_de_guerra}")
#                    break
#                raise Exception
#            except Exception:
#                print("O grito de guerra do time precisa ter, no máximo, 20 caracteres.")
#
#        while True:
#            try:
#                ano_de_fundacao = input(f"Qual o ano de fundação do time {i}? (Modelo de data: MM/dd/yyyy) ")
#                datetime.strptime(ano_de_fundacao, "%m/%d/%Y")
#                break
#            except:
#                print("O modelo de data não permitido. Use o formato indicado no exemplo.")
#        
#        time = TimesQuadribol(nome, grito_de_guerra, ano_de_fundacao)
#        times.append(time[i])
#
#    return times
#
#if __name__ == "__main__":
#    times = inserir_dados()
#    for time in times:
#        time.mostrar_informacoes_times()