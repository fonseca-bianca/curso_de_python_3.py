class Partida:
    duracao_partida = 180

    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        self.placar = {time1.nome: 50, time2.nome: 50}
        self.inicio = time.time()

    def atualizar_placar(self, time, pontos):
        if time in self.placar:
            self.placar[time] += pontos

    def registrar_ponto(self):
        evento = input(f"Registrar ponto para {self.time1.nome} ou {self.time2.nome}? (ex: blot, advrungh): ").lower()
        pontos = {"blot": 5, "plif": 1, "advrungh": -10, "expecto_patronum": 1}
        if evento in pontos:
            time_escolhido = input(f"Registrar ponto para qual time? ({self.time1.nome} ou {self.time2.nome}): ").strip()
            if time_escolhido in self.placar:
                self.atualizar_placar(time_escolhido, pontos[evento])
                print(f"{evento.capitalize()} registrado para {time_escolhido}.")
            else:
                print("Time não encontrado.")
        else:
            print("Evento desconhecido.")

    def iniciar_partida(self):
        print(f"Partida: {self.time1.nome} vs. {self.time2.nome}")
        while True:
            tempo_decorrido = time.time() - self.inicio
            tempo_restante = max(0, Partida.duracao_partida - int(tempo_decorrido))
            print(f"Tempo restante: {tempo_restante} segundos")

            if tempo_restante <= 0:
                print("A partida terminou.")
                break
            
            self.registrar_ponto()
        
        self.exibir_placar_final()

    def exibir_placar_final(self):
        print(f"Placar final: {self.time1.nome}: {self.placar[self.time1.nome]} vs. {self.time2.nome}: {self.placar[self.time2.nome]}")


if __name__ == "__main__":
    # Supõe que times já foram inseridos
    time1 = times[0]
    time2 = times[1]
    partida = Partida(time1, time2)
    partida.iniciar_partida()