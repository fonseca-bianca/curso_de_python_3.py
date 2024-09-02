
import time
from times_quadribol import TimesQuadribol

# cada partida terá 2 times se enfrentando
class Partida:
    # duração partida em segundos
    duracao_partida = 180

    # método construtor para encapsulamento, polimorfismo e melhor reutilização de código
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        self.placar = {time1.nome: 50, time2.nome: 50}
        self.inicio = time.time()
        # Início da partida
        # Cada time iniciará a partida com 50 pontos cada

    def encontrar_time_por_nome(self, nome):
        if nome == self.time1.nome:
            return self.time1
        elif nome == self.time2.nome:
            return self.time2
        else:
            print(f"Time '{nome}' não encontrado.")
            return None

    def atualizar_placar(self, nome_time, ponto):
        if nome_time in self.placar:
            self.placar[nome_time] += ponto
        else:
            print(f"Time '{nome_time}' não encontrado no placar.")

    def pontuacao(self):
        tempo_decorrido = time.time() - self.inicio
        tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))  # 180 segundos é o tempo total da partida

        if tempo_restante <= 0:
            print("A partida terminou.")
            return

        evento = {
            "blot": 5,
            "plif": 1,
            "advrungh": -10,
            "expecto_patronum": 1
        }

        while tempo_restante > 0:
            print("\nDigite o evento ocorrido ('blot', 'plif', 'advrungh', 'expecto_patronum'):")
            evento_usuario = input().strip()
            
            if evento_usuario not in evento:
                print("Evento inválido. Tente novamente.")
                continue

            print(f"Digite o nome do time que realizou o evento ({self.time1.nome} ou {self.time2.nome}):")
            nome_time = input().strip()

            time = self.encontrar_time_por_nome(nome_time)
            if time is None:
                continue

            ponto = evento[evento_usuario]
            self.atualizar_placar(nome_time, ponto)
            self.mostrar_placar()

            tempo_decorrido = time.time() - self.inicio
            tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))

    def mostrar_placar(self):
        print(f"Placar: {self.time1.nome}: {self.placar[self.time1.nome]} vs. {self.time2.nome}: {self.placar[self.time2.nome]}")