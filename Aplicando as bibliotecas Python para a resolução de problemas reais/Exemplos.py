# Impletmentar uma solução em Python para visualizar dados de 
# vendas de produtos em um grafico de barras


import matplotlib.pyplot as plt

x = ["A", "B", "C", "D"]
y = [3,8,1,10]


plt.bar(x, y)
plt.xlabel("x letras")
plt.ylabel("y numeros")
plt.title("grafico ex 01")
plt.show()