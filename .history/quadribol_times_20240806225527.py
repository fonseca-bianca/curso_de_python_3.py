from datetime import datetime

class Quadribol_Times:
    def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
        self.nome = nome
        self.grito_de_guerra = grito_de_guerra
        self.ano_de_fundacao = ano_de_fundacao

    def mostrar_informacoes_times(self):
        print(f"Nome do time: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}")

def criar_times():
    times = []
    for i in range(1, 2):
        while True:
            try:
                nome = input(f"Qual o nome do time {i}? ")
                if len(nome) <= 10:
                    print(f"O nome do time {i} é: {nome}")
                    break
                raise Exception
            except Exception:
                print("O nome do time precisa ter, no máximo, 10 caracteres.")
        
        while True:
            try:
                grito_de_guerra = input(f"Qual o grito de guerra do time {i}? ")
                if len(grito_de_guerra) <= 20:
                    print(f"O grito de guerra do time {i} é: {grito_de_guerra}")
                    break
                raise Exception
            except Exception:
                print("O grito de guerra do time precisa ter, no máximo, 20 caracteres.")

        while True:
            try:
                ano_de_fundacao = input(f"Qual o ano de fundação do time {i}? (Modelo de data: MM/dd/yyyy) ")
                datetime.strptime(ano_de_fundacao, "%m/%d/%Y")
                break
            except:
                print("O modelo de data não permitido. Use o formato indicado no exemplo.")
        
        time = Quadribol_Times(nome, grito_de_guerra, ano_de_fundacao)
        times.append(time)

    return times

if __name__ == "__main__":
    times = criar_times()
    for time in times:
        time.mostrar_informacoes_times()