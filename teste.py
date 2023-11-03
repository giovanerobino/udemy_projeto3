"""
teste.py - Arquivo para testes de funcionalidades.
"""
from models.cliente import Cliente
from models.conta import Conta


# instanciando o cliente
felicity: Cliente = Cliente("Felicity Jones", "fjones@ig.com.br", "123.456.789-00", "12/01/1990")
angelina: Cliente = Cliente("Angelina Jolie", "ajolie@ig.com.br", "123.456.789-00", "08/07/1978")

# vamos testar como o metodo __str__ funciona
# print(felicity)
# print(angelina)

# vamos testar como o metodo __str__ ta formatando
contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)

# voltar aqui depois testar os metodos depositar, sacar e transferir
