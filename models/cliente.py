"""
cliente.py - Arquivo para criação da classe cliente
"""
from datetime import date
from utils.helper import date_para_str, str_para_date


class Cliente:
    """ Classe que define um cliente. """


    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        """ Retorna o código do cliente. """
        return self.__codigo

    @property
    def nome(self: object) -> str:
        """ Retorna o nome do cliente. """
        return self.__nome

    @property
    def email(self: object) -> str:
        """ Retorna o email do cliente. """
        return self.__email

    @property
    def cpf(self: object) -> str:
        """ Retorna o cpf do cliente. """
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        """ Retorna a data de nascimento do cliente. """
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        """ Retorna a data de cadastro do cliente. """
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return (f'Código: {self.codigo} \n'
                f'Nome: {self.nome} \n'
                f'Data Nascimento: {self.data_nascimento} \n'
                f'Cadastrado em: {self.data_cadastro}')
