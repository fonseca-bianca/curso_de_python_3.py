"""
Exercício: 
criando um sistema de perguntas e respostas utilizando:
dict, list, tuple, for, while, function
"""


perguntas = [
    {
        "Pergunta": "Qual o resultado de 10 * 2?",
        "Opções": ["10", "20", "100"],
        "Resposta": "20",
    },
    {
        "Pergunta": "Qual o resultado de 150 / 2?",
        "Opções": ["17.5", "102", "75"],
        "Resposta": "75",
    },
    {
        "Pergunta": "Qual o resultado de 50 / 2?",
        "Opções": ["25", "12", "35"],
        "Resposta": "25",
    },
]

for pergunta in perguntas:
    print(pergunta["Pergunta"])
    print()

