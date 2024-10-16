"""
Exercício: 
criando um sistema de perguntas e respostas utilizando:
dict, list, tuple, for, while, function
"""

perguntas = [
    {
        "Pergunta": "Qual o resultado de 10 * 2?",
        "Opcoes": ["10", "20", "100"],
        "Resposta": "20",
    },
    {
        "Pergunta": "Qual o resultado de 150 / 2?",
        "Opcoes": ["17.5", "102", "75"],
        "Resposta": "75",
    },
    {
        "Pergunta": "Qual o resultado de 50 / 2?",
        "Opcoes": ["25", "12", "35"],
        "Resposta": "25",
    },
]

qtd_acertos = 0 
for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    
    opcoes = pergunta["Opcoes"]
    for i, opcao in enumerate(opcoes):
        letra = chr(97 + i)  # 97 é o código ASCII para 'a' e as demais o cód irá verificar automaticamente
        print(f"{letra}.", opcao)
    
    acertou = False
    escolha_str = None
    qtd_opcoes = len(opcoes)
    
    escolha_valida = False
    while not escolha_valida:
        escolha = input("Escolha uma opção: ")
        
        if escolha not in [chr(97 + i) for i in range(len(opcoes))]:
            print("Escolha inválida. Tente novamente.")
        else:
            escolha_valida = True
    
    print()
    index_escolha = ord(escolha) - 97 # ord('a') - 97 --> índice 0
    if opcoes[index_escolha] == pergunta["Resposta"]:
        qtd_acertos += 1
        print("Você acertou!")
    else:
        print("Você errou.")
    
    print()
    
print("Você acertou", qtd_acertos, "de", len(perguntas), "perguntas.")

# Função 'ord()': 
# retorna o código ASCII de um caractere --> ord('a') = 97
# Função 'chr()': 
# retorna o caractere correspondente ao código ASCII

