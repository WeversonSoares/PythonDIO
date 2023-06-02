from time import sleep
def ponto():
    print('Carregando sua requisição', end='')
    for i in range(3):
        print('.')
        sleep(0.8)
menu = '''
            ============================
            Olá, bem vindo ao banco nene
            ============================
               Escolha a melhor opção
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [0] Sair
            ============================
                     opção = '''
saldo = 0
extrato = ''
limite = 500
num_saques = 0
lim_saques = 3
while True:
    opcao = int(input(menu))
    if opcao == 1:
        valor = float(input('Digite um valor para depositar: R$'))
        if valor > 0:
            ponto()
            print(f'Valor de R${valor} depositado')
            saldo += valor
            extrato += f'Depósito: R${valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é invalido')
    elif opcao == 2:
        valor = float(input('Digite quanto deseja sacar: R$'))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques >= lim_saques
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente')
        elif excedeu_limite:
            print('Operação falhou! Valor digitado escede o valor de R$500,00')
        elif excedeu_saques:
            print('Operação falhou! Limite diario de saques atingido')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n' 
            num_saques += 1
        else: 
            print(' operação falhou! O valor informado é invalido')
    elif opcao == 3:
        print('''
            =========Extrato=========
            ''')
        print('''
        Não foram realizados movimentações''' if not extrato else extrato)
        print(f'Saldo R${saldo:.2f}')
        print('='*50)
    elif opcao == 0:
        break
    else:
        print('Falha! Operação invalida')
print('Obrigado por usar o banco nene')