"""
Este módulo contém a definição da classe Conta.
"""
from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:
    """ Classe que define uma conta. """


    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1


    def __str__(self: object) -> str:
        return (f"Número da conta: {self.numero} \n"
                f"Cliente: {self.cliente.nome}\n"
                f"Saldo Total: {formata_float_str_moeda(self.saldo_total)}")


    @property
    def numero(self: object) -> int:
        """ Retorna o número da conta. """
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        """ Retorna o cliente da conta. """
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        """ Retorna o saldo da conta. """
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        """ Retorna o limite da conta. """
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        """ Retorna o saldo total da conta. """
        return self.__saldo_total

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        """ Deposita o valor informado na conta. """
        pass

    def sacar(self: object, valor: float) -> None:
        """ Saca o valor informado da conta. """
        pass

    def transferir(self: object, destino: object, valor: float) -> float:
        """ Transfere o valor informado da conta. """
        pass
