"""
Exercício: 
criando um sistema de perguntas e respostas utilizando:
dict, list, tuple, for, while, function
"""

# lista q contém 3 dict.:
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

qtd_acertos = 0 # vai contar quantas perguntas o usuário acertou

# loop pra percorrer cada pergunta
for pergunta in perguntas: # pergunta e as opções de resposta
    print("Pergunta:", pergunta["Pergunta"])
    
    opcoes = pergunta["Opcoes"] # guarda as opções da pergunta atual
    for i, opcao in enumerate(opcoes):
        letra = chr(97 + i) # vai gerar as letras
        # 97 é o código ASCII para 'a' e as demais o cód irá verificar 
        # automaticamente
        print(f"{letra}.", opcao)
    
    # Inicializa variáveis de controle para validar entrada do usuário
    acertou = False
    escolha_str = None
    qtd_opcoes = len(opcoes)
    escolha_valida = False # verifica se a resposta do usuário está correta
    
    # Repete até o usuário digitar uma letra válida
    while not escolha_valida:
        escolha = input("Escolha uma opção: ")
        
        # Verifica se a letra digitada está entre as opções válidas
        if escolha not in [chr(97 + i) for i in range(len(opcoes))]:
            print("Escolha inválida. Tente novamente.")
        else:
            escolha_valida = True # Sai do loop se a escolha for válida
    
    print()
    index_escolha = ord(escolha) - 97 # converte letra escolhida em
    # número: ord('a') - 97 --> índice 0
    
    # Verifica se a opção escolhida é a resposta correta
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

