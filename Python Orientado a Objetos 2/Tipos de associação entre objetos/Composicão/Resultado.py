from Cliente import Cliente
from ContaClienteExtrato import Conta

cliente1 = Cliente(cpf= 12345,nome="joao", endereco="av imigrante")
cliente2 = Cliente(cpf= 54321,nome="Gio", endereco="Rua italia")

#Criando uma conta com dois clientes, fazendo a agregação com uma lista
conta1 = Conta(clientes=[cliente1, cliente2], numero=1, saldo=0)

conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)