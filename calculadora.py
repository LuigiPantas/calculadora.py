# Dando as boas vindas ao usuário
print("Bem vindo a calculadora do luigi!!!!")

# Mostrando quais operações estão disponiveis
print("Selecione a operação desejada: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Deixando o usuário escolher a operação desejada
operador = input("Digite o operador desejado: ")

# Declarando as variáveis como um numero decimal
num1 =float(input("Digite o primeiro número: "))
num2 =float(input("Digite o segundo número: "))

# Estrutura de decisão que executa a operação com base no operador escolhido
if  operador == "1":
    print(num1 + num2)
elif operador == "2":
    print(num1 - num2)
elif operador == "3":
    print(num1 * num2)
elif operador == "4":
    print(num1 / num2)
else:
    print("Operador inválido")
