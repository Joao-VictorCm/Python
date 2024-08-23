# Comunicação entre objetos na memoria
# Uma classe pode ter várias instancias(objetos) na memoria
# cada um com seus proprios valores de atributos
# Para comparar se duas referencias de memoria apontam para o mesmo objeto
# usamos os operadores == e !=


class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        

    def depositar(self, valor):
      self.saldo += valor  #incrementando

    def sacar(self, valor):
       self.saldo -= valor
    
    
    def gerar_extrato(self):
      print(f"Numero: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")
    
    
def main():
    conta1 = Conta(numero = 1, cpf = 123, nomeTitular = "João", saldo= 0)
    conta2 = Conta(numero = 2, cpf = 000, nomeTitular = "Gio", saldo= 100)
    
    if(conta1 != conta2):
        print("Endereços de memória diferentes")
    
    
    print(conta1)
    print(conta2)
    
    print(conta1.saldo)
    print(conta2.saldo)
    conta1.depositar(3000)
    print(conta1.saldo)
    
    
    
    
    
    #Igualando as duas contas(memos endereço de memeoria)
    conta1 = conta2
    
    print("Endereçõs iguais de memoria")
    
    print(conta1.saldo)
    print(conta2.saldo)
    
    
    
    
    
    
    
    
    
    

    
    
if __name__  == "__main__":
    main()
    