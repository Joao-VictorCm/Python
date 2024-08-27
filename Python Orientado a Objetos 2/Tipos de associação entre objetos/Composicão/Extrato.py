class Extrato:
    def __init__(self):
        self.transacoes = []  #Lista de transações da comta
        
        
    def extrato(self, numeroConta):
        print(f"Extrato:{numeroConta}")
        for transacao in self.transacoes:
            print(f"{transacao[0]:15s} {transacao[1]: 10.2f}")