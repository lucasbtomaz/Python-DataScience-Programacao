class Main:
    pass

print("Testando projeto")

from Classe.Cliente import Cliente
from Classe.Conta import Conta

c1 = Cliente("João da Silva", "123456789")
conta = Conta(c1._nome, 6565, 0)

print(c1.nome, " documento ", c1.cpf)
print(conta.titular, "Numero: ", conta.numero, "Seu saldo é de: ", conta.saldo)
