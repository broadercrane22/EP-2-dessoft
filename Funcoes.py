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

def calcula_pontos_soma(rolados):
    soma = 0
    for i in rolados:
        soma += i
    return soma

def calcula_pontos_sequencia_baixa(rolados):
    listas = [
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,6]
    ]
    seqbaixa = False
    for lista in listas:
        contador = 0
        if not seqbaixa:
            for i in lista:
                if i in rolados:
                    contador += 1
            if contador == 4:
                seqbaixa = True
    if seqbaixa:
        return 15
    else:
        return 0
def calcula_pontos_sequencia_alta(rolados):
    listas = [
        [1,2,3,4,5],
        [2,3,4,5,6],
    ]
    seqalta = False
    for lista in listas:
        contador = 0
        if not seqalta:
            for i in lista:
                if i in rolados:
                    contador += 1
            if contador == 5:
                seqalta = True
    if seqalta:
        return 30
    else:
        return 0