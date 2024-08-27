# Para atender a novas necessidades do sistema de conta corrente do banco, 
# agora é necessário adicionar uma funcionalidade para o gerenciamento de conta conjunta, 
# ou seja, uma conta corrente pode ter um conjunto de clientes associados. 
# Isso pode ser representado como uma agregação


class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clintes = clientes
        self.numero = numero
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return("Não existe saldo sufuciente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return("Transferencia Realizada")
        
    def gerarSaldo(self):
        print(f"numero:{self.numero} saldo:{self.saldo}")
        
        
