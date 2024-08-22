# Métodos com retorno
# serve para validar o estado de um objeto

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
    
    
def main():
    c1 = Conta(numero = 1, cpf= 00, nomeTitular= "João", saldo =1000)
    valor_saque = 300
    resultado_saque = c1.sacar(valor_saque)
    
    
    #Validando o retorno para verificar se o saque foi realizado
    if resultado_saque:
        print(f"Saque de R${valor_saque} realizado com sucesso")
        print(f"Saldo atual: R${c1.saldo}")
        
    else:
        print("Saldo insuficiente")
    
if __name__  == "__main__":
    main()