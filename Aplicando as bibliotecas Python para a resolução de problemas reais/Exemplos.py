# Exercico 01
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


# Exercico 02
# Implentar uma solução para gerar 1000 pontos seguindo a Distribuição Normal
# com media 20 e desvio padrão 
# Alem disso, exiba os dados em um hispograma

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
dados = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(dados, color= "lightblue", ec ="red")
plt.show()