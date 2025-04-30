import random

def rolar_dados(qnt):
    dados = []

    for i in range(qnt):
        dados.append(random.randint(1,6))
    return dados

def guardar_dado(rolados,guardados,dado):
    guardados.append(rolados[dado])
    del rolados[dado]
    return [rolados,guardados]

def remover_dado(rolados,guardados,indice):
    rolados.append(guardados[indice])
    del guardados[indice]
    return [rolados, guardados]

def calcula_pontos_regra_simples(faces):
    face = 1
    resultado = {}
    while face <= 6:
        quant = 0
        for valor in faces:
            if valor == face:
                quant += 1
        resultado[face] = quant*face
        face += 1
    return resultado