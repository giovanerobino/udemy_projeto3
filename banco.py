"""
Projeto: Banco
Descrição: Simulador de Banco
Versão: 0.1
"""
from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    """ Função chama a função menu() para ser mostrado no programa. """
    menu()


def menu() -> None:
    """ Menu com opções para o banco """
    print('===============================')
    print('============= ATM =============')
    print('======== Banco Nacional =======')
    print('===============================')

    print('Escolha uma das opções do menu')
    print('1 - Criar Conta')
    print('2 - Efetuar Saque')
    print('3 - Efetuar Deposito')
    print('4 - Efetuar Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Saindo do Sistema...')
        sleep(2)
        exit(0)
    else:
        print('Opção Inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    """ Cria uma conta cliente """
    print('Informe os dados do cliente: ')

    nome: str = input('Nome do Cliente: ')
    email: str = input('Email do Cliente: ')
    cpf: str = input('CPF do Cliente: ')
    data_nascimento: str = input('Data Nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso!')
    print('---- Dados da Conta: ----')
    print('-------------------------')
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    """ Função para sacar valor """
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))
            conta.sacar(valor)  # método de execução
        else:
            print(f'Não foi a encontrado a conta com número: {numero}')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    """ Função para efetuar depósito """
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))
            conta.depositar(valor)  # método de execução
        else:
            print(f'Não foi a encontrado a conta com número: {numero}')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    """ Função para efetuar transferências """
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta destino: '))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'Não foi encontrada a conta com número: {numero_d}')
        else:
            print(f'A sua conta com número: {numero_o} não foi encontrada.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def listar_contas() -> None:
    """ Função para listar as contas do sistema """
    if len(contas) > 0:
        print('Listagem de Contas:')

        for conta in contas:
            print(conta)
            print('-------------------------')
            sleep(1)
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    """ Função para percorrer as contas """
    c: Conta = None

    if len(contas) > 0:

        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c




if __name__ == '__main__':
    main()
