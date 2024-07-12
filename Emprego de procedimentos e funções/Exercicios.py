# Exercicio 01 

# Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista



def ehPar(n):
    r =(n%2==0)
    return r

def soma_pares(lista):
    soma = 0
    for num in lista:
        if(ehPar(num)):
            soma = soma + num
            return soma
        

lista_teste = [1, 2, 3, 5, 8]
soma = soma_pares(lista_teste)
print("Soma é: [{}]".format(soma))


# Exercicio 2

# Implementar uma solução em Python que calcule o fatorial de um número