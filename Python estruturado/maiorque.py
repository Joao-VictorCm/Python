##Implementar uma solução em Python que receba dois numeros e identifique qula o maior deles

a= 10
b=20

if(a > b):
    maior = a 
else:
    maior = b

    print(f"maior número é: {maior}")

""" Se a nota for maior ou igual a 7 aprovado
Se for menor que 7 e miaor ou igual a 5 recuperação
 se for menor que 5 reprovado
 """
nota = 5

if(nota >= 7):
    resultado = "Esta aprovado"
elif(nota >= 5):
    resultado = "Esta de recupeção"
else:
    resultado = "Esta reprovado"

print(f"o estudante esta: {resultado}")



""" Implementar uma solução que resolva a seguinte questão:
Calcular o valor de uma compra, sendo que o preço unitario é R$10,00
- Se dor comprado de ate 10 unidade, não há descontos.
- Para compras entre 11 e 20 unidades é dado um desconto de 10%
- Acima de 20 unidades, é dado um desconto de 20% """

preco_unitario = 10 
desconto10 = 0.1
desconto20 = 0.2
Qtd = eval(input("Digite a quantidade que vai comprar:"))

if(Qtd <= 10):
    valor_final = preco_unitario * Qtd

elif(Qtd <= 20):
    valor_final = preco_unitario*Qtd*(1-desconto10)

else:
    valor_final = preco_unitario*Qtd*(1-desconto20)

print(f"O valor final da compra é: {valor_final}")



