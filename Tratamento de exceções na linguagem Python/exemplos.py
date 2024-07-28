# Ex 01

# Implementas uma solução que faça o tratamento de excecão para verificar
# se a entrada é, de fato, um numero

try:
    x = int(input("Digite um número: "))

except ValueError:
    print("Entre com um número válido")
    
    
# Captura de exceções de múltiplos tipos

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")
    
    
# O tratamento completo das exceções

# try:
#   Bloco 1
# except Exception1:
#   Bloco tratador para Exception1
# except Exception2:
#   Bloco tratador para Exception1
# ...
# else:
#   Bloco 2 – executado caso nenhuma exceção seja levantada
# finally:
#   Bloco 3 – executado independente do que ocorrer
# Instrução fora do try/except