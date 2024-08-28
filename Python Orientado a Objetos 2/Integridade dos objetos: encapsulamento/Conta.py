#Somente pode ser alterado por um método da classe

class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero   #Atributo privado
        self.__saldo = saldo     #Atributo privado
        
    def main():
        conta = Conta(numero= 1, saldo= 100)
        saldo = conta.saldo
        print(saldo)
        
    if __name__== "__main__":
        main()