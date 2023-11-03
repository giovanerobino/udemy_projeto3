"""
formata datas e moedas
"""
from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    """ Converte um objeto date em uma data para o formato dd/mm/aaaa. """
    return data.strftime("%d/%m/%Y")


def str_para_date(data: str) -> date:
    """ Converte uma data no formato dd/mm/aaaa para o objeto date. """
    return datetime.strptime(data, "%d/%m/%Y")


def formata_float_str_moeda(valor: float) -> str:
    """ Formata um valor float para o formato R$ 0,00 """
    return f'R$ {valor:.2f}'.replace('.', ',')
