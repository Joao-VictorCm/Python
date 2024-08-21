#Criando uma Classe
# Contrutores e metodo init e self
# self e a forma da calsse se referir a ela mesmsa
# __init__ é o metodo construtor que cria o objeto da classe

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
 
 
        
# Instanciando um objeto conta
def main():
    c1 = Conta(numero= 1, cpf= 3, nomeTitular= "João", saldo= 100) 
    print(f"Nome do titular da conta:{c1.nomeTitular}")
    print(f"Numero da conta:{c1.numero}")
    print(f"Numero do Cpf do titular:{c1.cpf}")
    print(f"Saldo da conta:{c1.saldo}")
    
    
    

# Nesse caso, a condição do IF a seguir sera True
# Então o que esta no corpo do IF sera executado. no caso,
# é um chamado ao método main do script

if __name__ == "__main__":
    main()