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
    print("Pergunta 1:", pergunta["Pergunta"])
    print()

