def depositar(saldo: float, extrato: list, /) -> float:
    try:
        valor = int(input('Digite o valor do DEPÓSITO: '))
    except TypeError:
        print('ERRO! valor digitado não é decimal')

    if valor >= 1:
        saldo += valor
        valor_deposito = ['DEPOSITO', valor]
        extrato.append(valor_deposito)
    else:
        print('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')

    return saldo


def sacar(*, saldo: float, extrato: list, saques_diarios: int) -> tuple:
    try:
        valor = int(input('Digite um valor para o SAQUE: '))
    except TypeError:
        print('ERRO! valor digitado não é decimal')

    if saques_diarios == 3:
        print('ERRO! Seu limite de saques diários já ultrapassou 3')
    elif valor > 500:
        print('ERRO! Seu valor de saque ultrapassou o limite de R$500,00')
    elif valor < 1:
        print('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')
    elif valor > saldo:
        print('ERRO! Seu valor de saque é maior que o seu saldo total')
    else:
        saldo -= valor
        saques_diarios += 1
        valor_saque = ['SAQUE', valor]
        extrato.append(valor_saque)

    return saldo, saques_diarios


def mostrar_extrato(saldo: float, /, *, extrato: list, ) -> None:
    print('EXTRATO'.center(19, '-'))
    for tipo, valor in extrato:
        print(f'{tipo} de R${valor}')
    print(f'Saldo atual: R${saldo}')
