# #Exercicio 01
# #Escreva um programa que peça ao usuário para digitar um número. 
# #Trate o erro caso ele digite algo que não seja um número inteiro.

try:
    num1 = int(input("Digite um número: "))
except Exception:
    print("Digite apenas números inteiros. ex: 100")

#Exercicio 02
#Peça ao usuário dois números e tente multiplicá-los. 
#Se o usuário digitar algo inválido, exiba uma mensagem de erro.

try:
    num2 = float(input("numero 1 "))
    num3 = float(input("numero 2 "))
    resultado = num2*num3
except Exception:
    print("Digite apenas números")

# #Exercicio 03
# #Crie um programa que peça ao usuário um número inteiro. 
# #Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else

try:
    num4 = int(input("Digite um número inteiro: "))
    
except Exception:
    print("o número digitado não é inteiro")
else:
    print("A conversão foi bem sucedida")

#Exercicio 04
#Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

try:
    arquivo = "dados.txt"
    print(f"Abrindo arquivo {arquivo}")
finally:
    print(f"Encerrando programa")

# #Exercicio 05
# #Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError 
# # se b for igual a zero. Caso contrário, retorne o resultado da divisão.

 
def dividir():
    class erro_zero(ZeroDivisionError):
        pass
    try:
        a = float(input("Digite o dividendo: "))
        b = float(input("Digite o divisor "))
        if b == 0:
            raise erro_zero("o divisor não pode ser zero")
        else:
            resultado = a/b
            return resultado
        
    except TypeError:
        print("Digite apenas números")
    except erro_zero as erro:
        print(erro)
    
dividir()

# Exercicio 06
# Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) 
# que lance essa exceção caso a idade seja negativa.

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa")
    print(f" Idade {idade} cadastrada com sucesso!")

print("Tentando cadastrar uma idade válida")
try:
    cadastrar_idade(30)
except IdadeInvalidaError as invalida:
    print(f"ERRO: {invalida}")

print ("-" * 25)

print("tentando cadastrar idade inválida")
try:
    cadastrar_idade(-5)
except IdadeInvalidaError as invalida:
    print(f"ERRO: {invalida}")

# Exercicio 07
#Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:
#ValueError se o usuário digitar algo inválido
#ZeroDivisionError se tentar dividir por zero

class digito_invalido(ValueError):
    pass
class divisao_zero(ZeroDivisionError):
    pass

def divisao(num1,num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise digito_invalido ("Digite um número válido ")
    elif num2 == 0:
        raise divisao_zero ("Não é possível dividir por zero")
    else:
        resultado = num1/num2
        return resultado
    
try:
    resultado = divisao(100, 5)
    print(f"Resultado: {resultado}")
except (digito_invalido, divisao_zero) as e:
    print(f"Erro: {e}")

# 2. Teste de tipo inválido
print("\n--- Teste 2: Tipo inválido ---")
try:
    resultado = divisao(100, "texto")
except digito_invalido as e: # Capturando seu erro específico!
    print(f"Erro: {e}")

# 3. Teste de divisão por zero
print("\n--- Teste 3: Divisão por zero ---")
try:
    resultado = divisao(100, 0)
except divisao_zero as e: # Capturando seu outro erro específico!
    print(f"Erro: {e}")


# Exercicio 08
#Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
#    try para a conversão,
#    else para verificar se é par ou ímpar,
#    finally para exibir "Fim do programa".

try:
    numero = int (input("Digite um número inteiro: "))

except ValueError:
    print("Digite apenas números")

else:
    if numero % 2 != 0:
        print("O número é impar")
    else:
        print("O número é par")

finally:
    print("Fim do programa")

#Exercicio 09
#Crie uma função sacar(saldo, valor) que:
#Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
#Caso contrário, retorne o novo saldo. 
#Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.


class SaldoInsuficienteError (Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        # A mensagem é criada aqui
        raise SaldoInsuficienteError("Operação negada: Saldo Insuficiente.")
    else:
        return saldo - valor

1meu_saldo = 1000
print(f"Bem-vindo! Seu saldo atual é de R${meu_saldo}.")

# Teste 1: Saque com sucesso
try:
    valor_saque = 200
    meu_saldo = sacar(meu_saldo, valor_saque)
    print(f"Saque de R${valor_saque} realizado com sucesso.")
    print(f"Novo saldo: R${meu_saldo}.")
except SaldoInsuficienteError as e:
    print(e) # A mensagem do raise seria impressa aqui

print("-" * 25)

# Teste 2: Saque com falha
try:
    valor_saque = 2500
    print(f"Tentando sacar R${valor_saque}...")
    meu_saldo = sacar(meu_saldo, valor_saque)
except SaldoInsuficienteError as e:
    # A mensagem do raise é impressa aqui!
    print(e)
    print(f"Seu saldo continua: R${meu_saldo}.")