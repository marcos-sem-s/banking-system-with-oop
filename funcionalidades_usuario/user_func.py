def checar_cpf(cpf: str, users: list) -> None or str:
    for user in users:
        if cpf == user[2]:
            return None
    else:
        return cpf


def criar_usuario(users: list) -> None:
    cpf = input('Digite seu CPF: ')
    if not checar_cpf(cpf, users):
        print('ERRO! usuário já criado com este CPF')
        return
    elif not cpf.isnumeric():
        print('ERRO! CPF não numérico')
        return
    elif len(cpf) < 11:
        print('ERRO! CPF menor que 11 dígitos')
        return
    

    nome = input('Digite seu nome: ')
    birth_date = input('Digite sua data de nascimento [dd-mm-yy]: ')
    endereco= input('Digite seu endereço: [logradouro, n° - bairro - cidade/sigla estado]: ')

    users.append((nome, birth_date, cpf, endereco))


def criar_conta(users: list, contas: list, n_conta) -> None:
    cpf = input('Digite o CPF a ser integrado a conta: ')
    if checar_cpf(cpf, users):
        print('ERRO! CPF inexistente')
        return 0

    contas.append(('0001', n_conta, cpf))
    return 1


def see_users(users: list) -> None:
    for user in users:
        print(user)


def see_accounts(accounts: list) -> None:
    for account in accounts:
        print(account)
