import textwrap
from time import sleep
def ponto():
    print('\tCarregando sua requisição', end='')
    for i in range(3):
        print('.')
        sleep(0.8)


def menu():
    menu = f'''\n
        {'='*10}MENU{'='*10}
        Escolha a melhor opção
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNova conta
        [5]\tListar contas
        [6]\tNovo usuário
        [0]\tSair
        ===> '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
        ponto()
    else:
        print('@@@ Operação falhou! O valor informado é inválido. @@@')
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    if excedeu_saldo:
        print('@@@ Operação falhou! Saldo insuficiente @@@')
        ponto()
    elif excedeu_limite:
        print('@@@ Operação falhou! Limite insuficiente limite max de 500 reais@@@')
        ponto()
    elif excedeu_saques:
        print('@@@ Operação falhou! Você ja usou o limite maximo para saques @@@ \n@@@ Volte novamente amanha @@@')
        ponto()
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        ponto()
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Operação inválida! @@@')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print(f'\n{"="*10}EXTRATO{"="*10}')
    print('Não foram realizadas movimentações nas contas' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('='*27)


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (SOMENTE NÚMEROS): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('@@@ Já existe usuário utilizando este CPF')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Infome a data de nascimento do usuário (DDMMAAAA): ')
    endereco = input('Informe o endereço (logradouro, numero - bairro - cidade/ UF): ')
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, "endereco": endereco })
    ponto()
    print('=== Usuário Cadastrado com sucesso ===')
    ponto()


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        ponto()
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n@@@ Usuário não encontrado, fluxo de contas encerrado! @@@')
    ponto()


def listar_conta(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('='*27)
        print(textwrap.dedent(linha))


def main():
    LIMITES_SAQUES = 3
    AGENCIA = '0001'

    extrato = ''
    limite = 500
    saldo = 0
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()
        if opcao == '1':
            valor = float(input('Informe o valor do deposito: R$'))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == '2':
            valor = float(input('Informe o valor para saque: R$'))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITES_SAQUES
            )
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == '6':
            criar_usuario(usuarios)
        elif opcao == '4':
            numero_conta = len(contas)
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == '5':
            listar_conta(contas)
        elif opcao == '0':
            break
        else:
            print('Ops, opção inválida, tente novamente')
            ponto()


main()