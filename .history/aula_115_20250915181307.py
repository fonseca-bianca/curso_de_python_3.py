"""
O que são Ambientes Virtuais (venv)?
- venv: Creation of Virtual Environments:
    é criado em CADA projeto e não de forma global, justamente pra não travar
    a máquina ou pra não perder configurações originais de cada projeto
- carrega TODA a instação da LP pra uma pasta no caminho escolhido;
- a ser ativado, a instação do venv será usada;
- NÃO é enviada pro repositório remoto (gitignore);
    pode ser removida com uma pasta .gitignore na raiz do projeto;
- venv:
    é o módulo q será usado pra criar os ambientes virtuais;
- vc pode dar o nome q quiser pro ambiente virtual, mas os nomes mais comuns
são:
    venv
    env
    .venv
    .env
"""