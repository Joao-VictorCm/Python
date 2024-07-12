#  Implementar uma solução em Python que retorne o menor elemento de uma lista


def encontrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
            return minimo
        
lista_teste = [152, 2, 3, 55, 100]
menor = encontrar_minimo(lista_teste)
print("Menor elemento é: [{}]".format(menor))
        
        