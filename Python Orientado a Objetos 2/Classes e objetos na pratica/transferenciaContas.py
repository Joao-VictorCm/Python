# Transferencias entre contas
# criamos um método para a transferencias de valores

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        

    def depositar(self, valor):
      self.saldo += valor  #incrementando

    def sacar(self, valor):
       if self.saldo < valor:    #Validando se existe saldo para sacar
           return False
       else:
           self.saldo -= valor
           return True
    
    
    def gerar_extrato(self):
      print(f"Numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")
    
    
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return("Não eciste saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor 
            return("Transferencia Realizada")
        
            
def main():
    conta1 = Conta(numero = 1, cpf = 123, nomeTitular = "João", saldo= 1000)
    conta2 = Conta(numero = 2, cpf = 000, nomeTitular = "Gio", saldo= 500)
    
    
    print("saldo antes da TED")
    print(f"Saldo da conta 1:{conta1.saldo}")
    print(f"Saldo da conta 2:{conta2.saldo}")
    
    
    conta1.transfereValor(conta2, valor=300)
    print("saldo depois da TED")
    print(f"Saldo da conta 1:{conta1.saldo}")
    print(f"Saldo da conta 2:{conta2.saldo}")

    
if __name__  == "__main__":
    main()
    