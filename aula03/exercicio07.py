num1 = int( input("Digite o primeiro número: ") ) # chamando o input e já declarando a váriavel como tipo inteiro
num2 = input("Digite o segundo número: ") # Aqui cria o input mas não declara como variavel (reconhece string)
print(f"A soma de {num1} + {num2} = ", num1 + int(num2)) # int(num2) está convertendo o valor digitado no num2 de string pra inteiro
print(f"A Subtração de {num1} - {num2} = ", num1 - int(num2))
print(f"A Multiplicação de {num1} x {num2} = ", num1 * int(num2))
print(f"A Divisão de {num1} / {num2} = ", num1 / int(num2))