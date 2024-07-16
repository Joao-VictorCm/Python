# Exercicio 01 

# Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista



def ehPar(n):
    r =(n%2==0)  #Primeiro verificar quais numeros são pares
    return r

def soma_pares(lista):
    soma = 0
    for num in lista:
        if(ehPar(num)):
            soma = soma+num
            return soma
        

lista_teste = [1, 2, 3, 5, 4]
soma = soma_pares(lista_teste)
print("Soma é: [{}]".format(soma))


# Exercicio 2

# Implementar uma solução em Python que calcule o fatorial de um número

def fatorial_recursivo(n):
    if((n==0) or (n==1)):
        return 1
    return n*fatorial_recursivo(n-1)
   
    
numero = 4

print(f"o Fatorial de {numero} é: {fatorial_recursivo(numero)} ")


# Exercicio 3 
# Implementar uma solução em Python que determine se um Numero é ou não Primo


def ehPrimo(n):
    if(n<2):
        return False
    i=n//2
    while(i>1):
        if(n%i==0):
            return False
        i=i-1
        return True
    

def imprimirResultado(numero, resultado):
    mensagem = f"O numero {numero} Não é primo"
    if(resultado):
        mensagem= f"O numero {numero} é primo"
        return mensagem
    
numero = 5
resultado= ehPrimo(numero)
msg=imprimirResultado(numero, resultado)
print(msg)