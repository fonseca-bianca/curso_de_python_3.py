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
    
    for i, opcao in enumerate(pergunta["Opcoes"]):
        letra = chr(97 + i)  # 97 é o código ASCII para 'a' e as demais o cód irá verificar automaticamente
        print(f"{letra}.", opcao)
        
    escolha = input(f"Escolha uma opção: ")
    
    print()

