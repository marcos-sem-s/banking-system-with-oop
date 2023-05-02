from funcionalidades_usuario.user_func import *
from funcionalidades_conta.conta_func import *
from time import sleep


def menu() -> None:
    extrato = []
    usuarios = []
    contas = []
    n_conta = 1

    while True:
        escolha = int(input('''
Bem vindo ao Banco Marco&Iza
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Vizualizar usuários
[7] Vizualizar contas
[0] Sair
Digite: '''))

        if escolha == 1:
            saldo = depositar(saldo, extrato)
        elif escolha == 2:
            saldo, saques_diarios = sacar(saldo=saldo, extrato=extrato, saques_diarios=saques_diarios)
        elif escolha == 3:
            mostrar_extrato(saldo, extrato=extrato)
        elif escolha == 4:
            criar_usuario(usuarios)
        elif escolha == 5:
            n_conta += criar_conta(usuarios, contas, n_conta)
        elif escolha == 6:
            see_users(usuarios)
        elif escolha == 7:
            see_accounts(contas)
        elif escolha == 0:
            break
        else:
            print('Você digitou um número inválido, tente novamente')
        sleep(2)

    print('Grato pela preferência, até a próxima!')
