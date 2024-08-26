# Crie uma classe chamda televisão que receba siga os seguites requisitos:
# Receba como parametro em seu construtor o canal inicial, o maior canal
# Possua como atributos o canal sintonizado, io número do maior canal 
# Possua dois metodos um paradominuir o canl atual e o outro para aumentar o canl 
# instancie uma tv e teste a troca de canal 

class Televisão:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max
        
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal -= 1
        
        
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
        
        
tv1 = Televisão(pcanal= 2, min = 2, max = 10)
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)
    
tv2 = Televisão(pcanal= 10, min = 2, max = 10)
print(tv2.canal)
tv2.muda_canal_para_baixo()
print(tv2.canal)
    
        