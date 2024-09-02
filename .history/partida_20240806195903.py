import time

# Cada partida terá 2 times se enfrentando
class Partida:
    # Duração da partida em segundos
    duracao_partida = 180

    def __init__(self, time1, time2, valor_grito_time1, valor_grito_time2):
        self.time1 = time1
        self.time2 = time2
        self.valor_grito_time1 = valor_grito_time1
        self.valor_grito_time2 = valor_grito_time2
        self.placar = {time1: 50, time2: 50}  # Inicializa o placar com 50 pontos para cada time
        self.inicio = time.time()

    def encontrar_time_por_nome(self, nome):
        if self.time1.nome == nome:
            return self.time1
        elif self.time2.nome == nome:
            return self.time2
        print(f"Time '{nome}' não encontrado.")
        return None

    def atualizar_placar(self, time, ponto):
        if time in self.placar:
            self.placar[time] += ponto
        else:
            print(f"Time '{time.nome}' não está na partida.")

    def pontuacao(self, evento_time1, evento_time2):
        tempo_decorrido = time.time() - self.inicio
        tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))

        if tempo_restante <= 0:
            print("A partida terminou.")
            return

        eventos = {
            "blot": 5,
            "plif": 1,
            "advrungh": -10,
            "expecto_patronum": 1
        }

        if evento_time1 not in eventos or evento_time2 not in eventos:
            print("Eventos inválidos.")
            return

        ponto_time1 = eventos[evento_time1]
        ponto_time2 = eventos[evento_time2]

        # Atualiza os pontos dos times
        self.atualizar_placar(self.time1, ponto_time1)
        self.atualizar_placar(self.time2, ponto_time2)

        # Exibe as atualizações
        print(f"Time '{self.time1.nome}' evento: {evento_time1} ({ponto_time1} pontos)")
        print(f"Time '{self.time2.nome}' evento: {evento_time2} ({ponto_time2} pontos)")

    def mostrar_placar(self):
        print(f"Placar: {self.time1.nome}: {self.placar[self.time1]} vs. {self.time2.nome}: {self.placar[self.time2]}")