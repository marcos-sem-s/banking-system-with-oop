import logging 
from abc import ABC
from datetime import date


class Cliente:
    def __init__(self):
        self._endereco:str = None
        self._contas:list = None

    def realizar_transacao(self, conta:'Conta', transacao:'Transacao') -> None:
        pass

    def adicionar_conta(self, conta:'Conta') -> None:
        pass

class PessoaFisica(Cliente):
    def __init__(self):
        self._cpf:str = None
        self._nome:str = None
        self._data_nascimento:date = None

class Conta:
    def __init__(self):
        self._saldo: float = 1000
        self._numero: int = None
        self._agencia: str = '0001'
        self._cliente:'Cliente' = Cliente()
        self._historico:'Historico' = Historico()

    def saldo(self) -> float:
            print('SALDO'.center(20, '-'))
            # for tipo, valor in self.historico:
            #     print(f'{tipo} de R${valor}')
            # print(f'Saldo atual: R${self._saldo}')
            return self._saldo

    def nova_conta(cliente:'Cliente', numero:int) -> 'Conta':
        pass

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
            elif valor > self._saldo:
                logging.warning('ERRO! Seu valor de saque é maior que o seu saldo total')
            else:
                self._saldo -= valor
                self.saques_diarios -= 1
                valor_saque = ['SAQUE', valor]
                self.historico.append(valor_saque)
                
    def depositar(self, valor:float, /) -> bool:
        try:
            valor = float(valor)
        except TypeError:
            logging.exception('ERRO! valor digitado não é decimal')

        if valor > 0:
            self._saldo += valor
            valor_deposito = ('DEPOSITO', valor)
            self.historico.append(valor_deposito)
        else:
            logging.warning('ERRO! Não foi possível concluir a solicitação pois o valor é menor que 1')


class ContaCorrente(Conta):
    def __init__(self):
        self._limite: float = 500.00
        self._limite_saques: int = 3


class Transacao(ABC):
    def registrar(conta:'Conta'):
        pass


class Historico:
    def adicionar_transacao(self, transacao:'Transacao'):
        pass
    

class Deposito:
    def __init__(self) -> None:
        self._valor:float = None


class Saque:
    def __init__(self) -> None:
        self._valor:float = None
