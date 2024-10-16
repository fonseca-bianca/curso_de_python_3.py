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

for pergunta in perguntas:
    print("Pergunta:", pergunta["Pergunta"])
    
    opcoes = pergunta["Opcoes"]
    for i, opcao in enumerate(opcoes):
        letra = chr(97 + i)  # 97 é o código ASCII para 'a' e as demais o cód irá verificar automaticamente
        print(f"{letra}.", opcao)
        
    escolha = input("Escolha uma opção: ")
    
    acertou = False
    escolha_str = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isinstance(): # verifica se var 'escolha' é uma string
        escolha_str = str(escolha)
        
    if escolha_str is None:
        ...
    
    print()

