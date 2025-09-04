#Exercicio 01
# Crie uma função chamada saudacao que imprime na tela a mensagem "Olá, bem-vindo ao Python!". 
# Em seguida, chame a função no programa.

def saudacao():
    return "Olá, bem-vindo ao Python!"

print(saudacao())

#Exercicio 02
# Crie uma função chamada dobro que recebe um número como parâmetro e retorna o dobro desse número. 
# Teste chamando a função com diferentes valores.

def dobro(num):
    num += num
    return num

print(dobro(4))

#Exercicio 03
# Crie uma função chamada soma que receba dois números e retorne a soma deles.
# Depois, use a função para somar 10 + 20.

def soma(num1, num2):
    return num1+num2

print(soma(2,3))

#Exercicio 04
# Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

#     "Olá, [nome]!"

#          Caso o nome não seja informado, mostre "Olá, visitante!"

def mensagem(name=None):
    if not name:
        return "Olá, Visitante"
    else:
        return f"Olá, {name}"


print(mensagem())
print(mensagem("Andryus"))

#Exercicio 05
#Crie uma função chamada operacoes que receba dois números e retorne a soma,
#  a subtração e a multiplicação deles.

def operacoes(num1,num2):
    soma = f"A soma de {num1} + {num2} é: {num1+num2} " 
    subtracao = f"A subtração de {num1} - {num2} é: {num1-num2} " 
    multiplicacao = f"A multiplicação de {num1} x {num2} é: {num1*num2} "
    return f"{soma}\n{subtracao}\n{multiplicacao}"

print(operacoes(2,5))

#Exercicio 06
#Crie uma função chamada media que receba uma quantidade variável de números 
# e retorne a média deles.
# Teste com 3, 5 e 7 valores diferentes

def media(*args):
    media = sum(args) / len(args)
    return media

print(media(3,5,7))

#Exercicio 07
# Crie uma função chamada dados_pessoais que receba informações de uma pessoa (nome, idade, cidade, etc.) usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:

# dados_pessoais(nome="Ana", idade=25, cidade="Recife")

def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print( f"{chave}: {valor}\n ")

print(dados_pessoais(nome="Ana", idade=25, cidade="Recife"))

# Exercicio 08
# Crie uma função chamada calculadora que tenha dentro dela outras funções (somar, subtrair, multiplicar, dividir). A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora(operacao, *args):
    def somar():
        soma = sum(args)
        return soma
    def subtrair():
        total = args[0]
        #Inicia um loop que percorre todos os números em 'args', EXCETO o primeiro 
        for num in args[1:]: # (slicing)
            total = total-num
        return total 
    def multiplicar():
        resultado = 1
        for num in args:
            resultado = resultado*num
        return resultado 
    def dividir():
        div = args[0]
        for num in args[1:]:
            div = div/num
        return div
    pass

    if operacao == "somar":
        return somar()
    elif operacao == "subtrair":
        return subtrair()
    elif operacao == "multiplicar":
        return multiplicar()
    elif operacao == "dividir":
        return dividir()
    else:
        return "Operação Inválida"
    pass

print(calculadora("multiplicar", 2,5,3,10))

#Exercicio 09
#Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:

#  def soma(a, b): return a + b
#  aplicar_operacao(3, 4, soma)

def aplicar_operacao(num1, num2, funcao_operacao):
    return funcao_operacao(num1,num2)

def soma(a,b): return a + b

def multiplicar(c,d): return c * d

print(aplicar_operacao(3,4, multiplicar))
