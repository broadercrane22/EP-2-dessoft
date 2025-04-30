import random

def rolar_dados(qnt):
    dados = []

    for i in range(qnt):
        dados.append(random.randint(1,6))
    return dados

