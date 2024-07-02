# ATRIBUIÇÃO MÚLTIPLA

a , b = 1, 2
print("Antes da troca")  
print(f"o valor das variaveis: a={a}, b={b}") #Retorna a=1  e b=2


#Primeira troca

temp = a
a = b
b =  temp
print("Primeria troca")
print(f'O valor das variaveis é: a={a}, b={b}')  #Retorna a=2  e b=1


#Segunda troca

a,b = b,a
print("Primeria troca")
print(f'O valor das variaveis é: a={a}, b={b}')  #Retorna a=1  e b=2