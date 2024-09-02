# """
# Repetições WHILE e BREAK:
# while: executa ação enquanto for TRUE
# *looping infinito: quando condição NÃO tem fim/pausa
# break: para o bloco
# """

# condicao = True

# while condicao:
#     nome = input("Digite o seu nome: ")
#     print(f"O seu nome é {nome}")
    
#     resposta = input("Digite 'sair' pra fechar o programa: ")
#     if resposta == "sair":
#         break 

# print("Programa encerrado\n")
# """
# se NÃO colocar esse Break aq, o programa vai pedir a mesma coisa infinitamente,
# pois a condição estabelecida é True, ou seja, necessitaria de uma condição seguinte
# False ou outra condição True ou se um Break pra ocorrer sua interrupção
# """




def aplicar_advrungh(self):
	if self.tipo_de_irregularidade == "bateu_2_vezes":
		print("O jogador cometeu irregularidade, pois bateu 2x na bola na mesma jogada.")
	elif self.tipo_de_irregularidade == "invasao_quadra":
		print("Houve irregularidade por parte da torcida adversária, porque invadiu a quadra durante o jogo.")

		penalidade_time = self.irregularidade_time
		print(f"Houve irregularidade causada pelo time {penalidade_time.nome} adversário.")
		self.placar[self.time1 == penalidade_time] -= 10
		self.placar[self.time2 == penalidade_time] -= 10
		self.houve_irregularidade = False
		return self.time_vencedor()

    