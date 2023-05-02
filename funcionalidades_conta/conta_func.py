import logging 

class Conta:
    def __init__(self):
        self._saldo: float = 1000
        self._numero: int = None
        self._agencia: str = '0001'
        self._historico = []

    def depositar(self, valor:float, /) -> bool:
        try:
            valor = float(valor)
        except TypeError:
            logging.exception('ERRO! valor digitado não é decimal')

        if valor > 0:
            self.saldo += valor
            valor_deposito = ('DEPOSITO', valor)
            self.historico.append(valor_deposito)
        else:
            logging.warning('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')

    def sacar(self, *, valor:float) -> bool:
        try:
            valor = float(valor)
        except TypeError:
            logging.exception('ERRO! valor digitado não é decimal')

        if self.saques_diarios == 0:
            logging.warning('ERRO! Seu limite de saques diários já ultrapassou 3')
        elif valor > 500:
            logging.warning('ERRO! Seu valor de saque ultrapassou o limite de R$500,00')
        elif valor < 1:
            logging.warning('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')
        elif valor > self.saldo:
            logging.warning('ERRO! Seu valor de saque é maior que o seu saldo total')
        else:
            self.saldo -= valor
            self.saques_diarios -= 1
            valor_saque = ['SAQUE', valor]
            self.historico.append(valor_saque)

    def saldo(self) -> None:
        print('SALDO'.center(20, '-'))
        for tipo, valor in self.historico:
            print(f'{tipo} de R${valor}')
        print(f'Saldo atual: R${self.saldo}')


class ContaCorrente(Conta):
    def __init__(self):
        self._limite: float = 500.00
        self._limite_saques: int = 3


class Historico(Conta):
    # def __init__(self):
    #     self._limite: float = 500.00
    #     self._limite_saques: int = 3
    pass
