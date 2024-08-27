import datetime
from Extrato import Extrato

class Conta:
    def __inti__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()  #Iniciando Composição
        
        
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor, "Data", datetime.datetime.today()])
    
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor, "Data", datetime.datetime.today() ])
            
    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return False
        else:
           contadestino.depositar(valor)
           self.saldo -= valor
           self.extrato.transacoes.append(["Transferencia", valor, "Data", datetime.datetime.today() ])
           
    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")