extrato = []
LIMITE = 500
saldo = 1000
saques_diarios = 0

def deposito():
    global saldo

    try:
        valor = int(input('Digite o valor do depósito: '))
    except:
        print('ERRO! Houve um problema com o tipo do valor digitado')

    if valor >= 1:
        saldo += valor
        valor_deposito = ['DEPOSITO', valor]
        extrato.append(valor_deposito)
    else:
        print('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')


def saque():
    global saldo, saques_diarios

    try:
        valor = int(input('Digite o valor do saque: '))
    except:
        print('ERRO! Houve um problema com o tipo do valor digitado')

    if saques_diarios == 3:
        print('ERRO! Seu limite de saques diários já ultrapassou 3')
    elif valor > LIMITE:
        print('ERRO! Seu valor de saque ultrapassou o limite de R$500,00')
    elif not valor > 1:
        print('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')
    elif valor > saldo:
        print('ERRO! Seu valor de saque é maior que o seu saldo total')
    else:
        saldo -= valor
        saques_diarios += 1
        valor_saque = ['SAQUE', valor]
        extrato.append(valor_saque)


def mostrar_extrato(extrato:list):
    print('EXTRATO'.center(19, '-'))
    for i in extrato:
        print(i)
    print(f'Saldo atual: R${saldo}')


while True:
    escolha = int(input('''
Bem vindo ao BANCO PROENÇA
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
Digite: '''))

    if escolha == 1:
        deposito()
    elif escolha == 2:
        saque()
    elif escolha == 3:
        mostrar_extrato(extrato)
    elif escolha == 0:
        break
    else:
        print('Você digitou um número inválido, tente novamente')
