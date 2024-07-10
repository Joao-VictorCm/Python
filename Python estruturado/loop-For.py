nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)


##while

nome = input("entre com uma palavra")

while palavra != "sair":
    palavra = input("Digite sair para encerrar")
    print("Voçê digitiou sair")



# O laço while infinito

while True:
    print("ola")


##As instruções auxiliares break, continue e pass 

# while True: 
#     palavra = input('Entre com uma palavra: \n')
#     if palavra == 'sair':
#         break
#     print('Você digitou sair e agora está fora do laço')


# # Ex 2 


# while True:
#     print('Você está no primeiro laço.')
#     opcao1 = input('Deseja sair dele? Digite SIM para isso. \n')
#     if opcao1 == 'SIM':
#         break  # este break é do primeiro laço
#     else:


##A instrução continue

# for num in range(1, 11):
#     if num == 5:
#         continue
#     else:
#         print(num)
# print("encerrado")



# ##A instrução pass

#for num in range(1, 11):
#     if num % 2 == 0:
#         pass
#     else:
#         print(num)
# print('Laço encerrado')


