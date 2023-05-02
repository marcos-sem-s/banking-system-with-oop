# import json

# db = {'nome': 'Marco', 'idade': 19}

# def digitar_float(tipo):
#     if tipo == 'deposito':
#         valor = input('Digite um valor para o DEPÓSITO: ')
#     elif tipo == 'saque':
#         valor = input('Digite um valor para o SAQUE: ')

#     while not valor.isnumeric():
#         valor = input('ERRO! Digite um valor decimal válido: ')

# with open('storage.json', 'w') as arq:
#     over = json.dumps(db, indent=4)
#     arq.write(over)

# with open('storage.json', 'r') as arq:
#     over = json.load(arq)
#     print(len(over))

if __name__ == '__main__':

    from funcionalidades_conta import Conta

    conta01 = Conta()
    while True:
        conta01.depositar(input('Digite o valor do DEPÓSITO: R$'))
        conta01.sacar(valor = input('Digite o valor do SAQUE: R$'))
        conta01.mostrar_extrato()
