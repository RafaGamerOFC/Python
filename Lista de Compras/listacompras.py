import os


# Função para limpar o console
def clear():
    print('\n' * 100)
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para salvar a lista de compras em um arquivo de texto
def salvar_lista(nomes, valores):
    with open('lista_compras.txt', 'w') as arquivo:
        for nome, valor in zip(nomes, valores):
            arquivo.write(f"{nome},{valor}\n")


# Função para carregar a lista de compras do arquivo ao iniciar o programa
def carregar_lista():
    nomes = []
    valores = []
    try:
        with open('lista_compras.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome, valor = linha.strip().split(',')
                nomes.append(nome)
                valores.append(float(valor))
    except FileNotFoundError:
        # Se o arquivo ainda não existir, retorna listas vazias
        return [], []
    return nomes, valores


# Inicializa as listas com os dados do arquivo, se existirem
nomes, valores = carregar_lista()

while True:
    clear()
    print('=' * 45)
    print(f'{"LISTA DE COMPRAS":^45}')
    print('=' * 45)
    print("""
[ 1 ] Adicionar item
[ 2 ] Remover item
[ 3 ] Ver lista de compras
[ 4 ] Sair do programa
""")
    menu = str(input('Qual sua escolha? ')).strip()
    if menu == '1':
        while True:
            clear()
            print('=' * 45)
            print(f'{"ADICIONAR ITEM":^45}')
            print('=' * 45)
            while True:
                nome_produto = str(input('Digite o nome do produto: ')).strip()
                if nome_produto != '':
                    break
            while True:
                try:
                    valor_produto = str(input('Digite o valor: ')).strip()
                    valor_produto = valor_produto.replace(",", ".")
                    valor_produto = float(valor_produto)
                    break
                except ValueError:
                    print('Por favor, digite um valor válido.')

            nomes.append(nome_produto)
            valores.append(valor_produto)
            print('Valor adicionado com sucesso...')
            escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
            if escolha == 'N':
                break
        # Após adicionar, salva a lista em um arquivo
        salvar_lista(nomes, valores)
    if menu == '2':
        clear()
        print('=' * 45)
        print(f'{"REMOVER ITEM":^45}')
        print('=' * 45)
        cont = 0
        for mostrar in nomes:
            print(cont, ' - ', nomes[cont])
            cont += 1
        print('=' * 45)
        while True:
            while True:
                try:
                    deletar = int(input('\nDigite o número da lista que deseja remover: '))
                    break
                except ValueError:
                    print('Por favor digite um valor válido.')
            if deletar < 0 or deletar >= len(nomes):
                print('Índice inválido. Por favor, escolha um número dentro do intervalo válido.')
            else:
                print(f'O item {nomes[deletar]} foi deletado com sucesso da lista de compras.')
                del nomes[deletar]
                del valores[deletar]
                break
        input('\nAperte ENTER para continuar.')
        # Após remover, salva a lista em um arquivo
        salvar_lista(nomes, valores)
    if menu == '3':
        clear()
        print('=' * 45)
        print(f'{"VER LISTA DE COMPRAS":^45}')
        print('=' * 45)
        cont = 0
        for qnt in nomes:
            print(f'{nomes[cont]:.<35}', end='')
            print(f'R${valores[cont]:>8.2f}')
            cont += 1
        print('=' * 45)
        input('\nAperte ENTER para continuar.')
    if menu == '4':
        clear()
        print('=' * 45)
        print('Encerrando sistema!')
        break
