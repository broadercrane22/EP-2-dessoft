import funcoes as fun
combinacoesutilizadas = []
combinacoespossiveis = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        'sem_combinacao',
        'quadra',
        'full_house',
        'sequencia_baixa',
        'sequencia_alta',
        'cinco_iguais'
]
cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
fun.imprime_cartela(cartela)
naopreencheu = True
while naopreencheu:
    usou2rerolls = False
    quantidadererolls = 0
    guardados = []
    dados = fun.rolar_dados(5)
    print(f'Dados rolados: {dados}')
    print(f'Dados guardados: {guardados}')
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    opcao = input()
    while opcao not in ('0','1','2','3','4'):
        print("Opção inválida. Tente novamente.")
        opcao = input()
    while opcao != '0':
        if opcao == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            guardar = int(input())
            if guardar < len(dados):
                dados, guardados = fun.guardar_dado(dados, guardados, guardar)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            opcao = input()
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            remover = int(input())
            if remover < len(guardados):
                dados, guardados = fun.remover_dado(dados, guardados, remover)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            opcao = input()
        elif opcao == '3':
            if not usou2rerolls:
                dados = fun.rolar_dados(5-len(guardados))
                print(f'Dados rolados: {dados}')
                print(f'Dados guardados: {guardados}')
                quantidadererolls += 1
                if quantidadererolls == 2:
                    usou2rerolls = True
                print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
                opcao = input()
            else:
                print("Você já usou todas as rerrolagens.")
                print(f'Dados rolados: {dados}')
                print(f'Dados guardados: {guardados}')
                print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
                opcao = input()
        elif opcao == '4':
            fun.imprime_cartela(cartela)
            print(f'Dados rolados: {dados}')
            print(f'Dados guardados: {guardados}')
            print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
            opcao = input()
    if opcao == '0':
        combinacaovalida = False
        print("Digite a combinação desejada:")
        combinacao = input()
        while not combinacaovalida:
            if combinacao not in combinacoespossiveis:
                print("Combinação inválida. Tente novamente.")
                combinacao = input()
            elif combinacao in combinacoesutilizadas:
                print("Essa combinação já foi utilizada.")
                combinacao = input()
            else:
                combinacaovalida = True
        cartela = fun.faz_jogada(dados, combinacao, cartela)
        combinacoesutilizadas.append(combinacao)
    if -1 not in cartela['regra_simples'].values() and -1 not in cartela['regra_avancada'].values():
        naopreencheu = False
pontuacaoregrasimples = 0
pontuacaototal = 0
for pontos in cartela['regra_simples'].values():
    pontuacaoregrasimples += pontos
    pontuacaototal += pontos
for pontos in cartela['regra_avancada'].values():
    pontuacaototal += pontos
if pontuacaoregrasimples >= 63:
    pontuacaototal += 35
fun.imprime_cartela(cartela)
print(f'Pontuação total: {pontuacaototal}')




