# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')


# Análise de trecho de código:

# acertou = False
    # Cria uma variável booleana que indica se a resposta está correta ou não.
    # Começa como False, e só será True se o usuário acertar a resposta.

# escolha_int = None
    # Cria a variável que vai armazenar a escolha do usuário como número 
    #   int (índice da opção escolhida).
    # Começa como None, e depois será convertida (ex: de "2" para 2) caso 
    #   o usuário digite um número válido.

# qtd_opcoes = len(opcoes)
    # Armazena quantas opções existem naquela pergunta, usando len().
    # Serve para validar se a escolha do usuário está dentro do intervalo 
    #   permitido (ex: 0 a 3 se houver 4 opções).
