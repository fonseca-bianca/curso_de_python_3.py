def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
        self.nome = nome
        self.grito_de_guerra = grito_de_guerra
        self.ano_de_fundacao = ano_de_fundacao

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}")

def inserir_nomes():
    times = []
    for i in range(1, 9):
        while True:
            try:
                nome = input(f"Qual o nome do time {i}? ")
                if len(nome) > 10:
                    raise ValueError("Número máximo de caracteres ultrapassado")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                grito_de_guerra = input(f"Qual o grito de guerra do time {i}? ")
                if len(grito_de_guerra) > 20:
                    raise ValueError("Número máximo de caracteres ultrapassado")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                ano_de_fundacao = input(f"Qual o ano de fundação do time {i} (MM/dd/yyyy)? ")
                # Verifica se a data está no formato MM/dd/yyyy
                from datetime import datetime
                datetime.strptime(ano_de_fundacao, "%m/%d/%Y")
                break
            except ValueError:
                print("Modelo de data não permitido. Por favor, use o formato MM/dd/yyyy.")

        time = Time(nome, grito_de_guerra, ano_de_fundacao)
        times.append(time)
    return times

# Coleta e exibe as informações dos times
times = inserir_nomes()
for time in times:
    time.mostrar_info()