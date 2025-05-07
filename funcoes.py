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
    
    #lalalala

def calcula_pontos_full_house(dados):
    if len(dados) != 5:
        return 0

    contagem = {}
    for numero in dados:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    encontrou_3 = False
    encontrou_2 = False
    for valor in contagem.values():
        if valor == 3:
            encontrou_3 = True
        elif valor == 2:
            encontrou_2 = True

    if encontrou_3 and encontrou_2:
        total = 0
        for num in dados:
            total += num
        return total
    else:
        return 0
    
def calcula_pontos_quadra(dados):
    contagem = {}
    for numero in dados:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    tem_quadra = False
    for valor in contagem.values():
        if valor >= 4:
            tem_quadra = True
            break

    if tem_quadra:
        total = 0
        for num in dados:
            total += num
        return total
    else:
        return 0

def calcula_pontos_quina(dados):
    contagem = {}
    for numero in dados:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1

    for valor in contagem.values():
        if valor >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }
def faz_jogada(dados, categoria, cartela):
    if len(categoria) == 1:
        categoria = int(categoria)
    if categoria in cartela['regra_simples']:
        cartela['regra_simples'][categoria] = calcula_pontos_regra_simples(dados)[categoria]
    elif categoria in cartela['regra_avancada']:
        cartela['regra_avancada'][categoria] = calcula_pontos_regra_avancada(dados)[categoria]
    return cartela
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
