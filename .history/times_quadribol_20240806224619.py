import random
from datetime import datetime

class TimesQuadribol:
    """Representa um time de Quadribol.

    Atributos:
        nome (str): O nome do time.
        grito_de_guerra (str): O grito de guerra do time.
        ano_de_fundacao (str): O ano de fundação do time no formato MM/DD/YYYY.
        pontos (int): A pontuação total do time no torneio.
    """

    def __init__(self, nome, grito_de_guerra, ano_de_fundacao):
        self.nome = nome
        self.grito_de_guerra = grito_de_guerra
        self.ano_de_fundacao = ano_de_fundacao
        self.pontos = 0  # Inicializa a pontuação do time

    def mostrar_informacoes_times(self):
        """Exibe as informações de um time."""
        print(f"Nome do time: {self.nome}, Grito de Guerra: {self.grito_de_guerra}, Ano de Fundação: {self.ano_de_fundacao}, Pontos: {self.pontos}")

def criar_times():
    """Cria uma lista de times de Quadribol."""
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
        
        time = TimesQuadribol(nome, grito_de_guerra, ano_de_fundacao)
        times.append(time)

    return times

if __name__ == "__main__":
    times = criar_times()
    for time in times:
        time.mostrar_informacoes_times()
        
        def sortear_times(times, num_times_sortear):
            """Args:
        times: Uma lista de objetos TimesQuadribol.
        num_times_sortear: O número de times a serem sorteados.

    Returns:
        Uma lista com os times sorteados.
    """
    times_sorteados = []
    for _ in range(num_times_sortear):
        if not times:
            print("Não há mais times para sortear.")
            break
        time_sorteado = random.choice(times)
        times_sorteados.append(time_sorteado)
        times.remove(time_sorteado)
    return times_sorteados