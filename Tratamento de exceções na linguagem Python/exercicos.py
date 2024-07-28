# Ex 01

# Implementas uma solução que faça o tratamento de excecão para verificar
# se a entrada é, de fato, um numero e que, alem disso, insista que o usuario
# digite um Numero valido

   
while True:
    try:
       x = int(input("Digite um número: "))
       break
    except ValueError:
      print("Entre com um número válido")
   

# Ex 02

# Implementar uma solução que faça o tratamento de excecão de divisão por Zero

def dividir(x, y):

 try:
    resultado = x / y
    print("A resposta é:", resultado)
 except ZeroDivisionError:
    print("Divisão por zero")
    
    
dividir(3, 0)