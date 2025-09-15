# Exercicio 01
# Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos
# dessa classe e imprima os valores de seus atributos.

class Pessoa:
   def __init__(self, nome, idade):
     self.nome = nome
     self.idade = idade
     pass 

carlos = Pessoa("Carlos", 12)
roberto = Pessoa("Roberto", 22)

print(roberto.nome, roberto.idade)
print(carlos.nome, carlos.idade)

# Exercicio 02
# Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:
# "Olá, meu nome é João e tenho 25 anos.".
#  Teste o método chamando-o a partir de um objeto.

class Pessoa:
    def __init__(self, nome, idade):
     self.nome = nome
     self.idade = idade
     pass
    def apresentar (self):
       print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

persona = Pessoa("Patrick", 18)
persona.apresentar()

# Exercicio 03
# Crie uma classe Carro com os atributos marca, modelo e ano. 
# Use o método __init__ para inicializar esses valores.
# Crie três objetos e mostre suas informações.

class Carro:
    def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano
    def __str__(self):
        return f"Marca = {self.marca}, modelo = {self.modelo} , ano = {self.ano}"

carro1 = Carro("Honda", "Civic", 2008)
carro2 = Carro("Toyota", "Corolla", 2012)
carro3 = Carro("Dodge", "Ram", 2020)

print(carro1)
print(carro2)
print(carro3)

# Exercicio 04
# Usando a classe Carro, crie um objeto e depois altere o valor de um de 
# seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.

class Carro:
    def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano
    def __str__(self):
        return f"Marca = {self.marca}, modelo = {self.modelo} , ano = {self.ano}"

carro1 = Carro("Honda", "Civic", 2008)

print(carro1)

carro1.ano = 2025

print(carro1)

# Exercicio 05
# Crie uma classe ContaBancaria com os atributos titular e saldo. 
# Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) 
# que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.

class ContaBancaria:
  #Atributos
  def __init__(self, titular, num_conta, saldo=0): # Função construtora
      self.titular = titular
      self.saldo = saldo
      self.num_conta = num_conta
  def depositar(self,valor):
     self.saldo += valor
  def sacar(self,valor):
     if valor > self.saldo:
        print("Operação Negada: Saldo Insuficiente")
     else:
        self.saldo -= valor

conta_andryus = ContaBancaria(titular = "Andryus Esteves", num_conta="24245-6", saldo = 1500)

conta_andryus.depositar(120)

conta_andryus.sacar(150)
print("Saque Realizado com sucesso")

conta_andryus.sacar(5000)

print(f"Saldo final na conta de {conta_andryus.titular}: R$ {conta_andryus.saldo}")

# Exercicio 06
# Modifique a classe ContaBancaria para que o método sacar retorne True 
# se a operação for bem-sucedida e False caso contrário. 
# Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
  #Atributos
  def __init__(self, titular, num_conta, saldo=0): # Função construtora
      self.titular = titular
      self.saldo = saldo
      self.num_conta = num_conta
  def depositar(self,valor):
     self.saldo += valor
  def sacar(self,valor):
     if valor > self.saldo:
        print("Operação Negada: Saldo Insuficiente")
        return False 
     else:
        print("Operação Realizada com sucesso!")
        self.saldo -= valor
        return True

print("--- Iniciando Simulação ---")
conta_ana = ContaBancaria(titular="Ana Paula", num_conta="555-7", saldo=2000)
print(f"Conta criada para {conta_ana.titular} com saldo de R${conta_ana.saldo}.")

print("\n--- Teste 1: SAQUE VÁLIDO ---")
valor_saque_valido = 500
print(f"Tentando sacar R${valor_saque_valido}...")

# 1. Chamamos o método e guardamos a resposta (True ou False) na variável 'sucesso'
sucesso = conta_ana.sacar(valor_saque_valido)

# 2. Usamos a resposta para decidir qual mensagem exibir
if sucesso:  # Isso é o mesmo que 'if sucesso == True:'
    print(f"[Teste]: O saque foi BEM-SUCEDIDO.")
    print(f"Saldo atualizado: R${conta_ana.saldo}")
else:
    print(f"[Teste]: O saque FALHOU.")

print("\n" + "-"*30 + "\n")

print("--- Teste 2: SAQUE INVÁLIDO ---")
valor_saque_invalido = 3000
print(f"Tentando sacar R${valor_saque_invalido}...")

# 3. Chamamos o método novamente e guardamos a nova resposta
sucesso = conta_ana.sacar(valor_saque_invalido)

# 4. Usamos a nova resposta para decidir o que fazer
if sucesso:
    print(f"[Teste]: O saque foi BEM-SUCEDIDO.")
else:
    print(f"[Teste]: O saque FALHOU, como era esperado.")


print(f"\nSaldo final na conta: R${conta_ana.saldo}")


# Exercicio 07
#Crie uma classe Aluno com atributos nome e nota. 
# Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno).
#  Crie alguns objetos Aluno e adicione-os à turma.

class Aluno:
   def __init__(self, nome, nota):
      self.nome = nome
      self.nota = nota
      
class Turma:
    def __init__(self):
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

aluno1 = Aluno("Andryus", 2)
aluno2 = Aluno("Carlos", 9)

turma_python = Turma()

turma_python.adicionar_aluno(aluno1)
turma_python.adicionar_aluno(aluno2)

for aluno in turma_python.alunos:
   print(f"Nome do aluno: {aluno.nome} nota {aluno.nota}")

# Exercicio 08
#Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, 
# apareça algo como:
# "Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def __str__(self):
       return f"Aluno: {self.nome} - Nota: {self.nota} "
      
class Turma:
    def __init__(self):
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

aluno1 = Aluno("Andryus", 2)
aluno2 = Aluno("Carlos", 9)

turma_python = Turma()

turma_python.adicionar_aluno(aluno1)
turma_python.adicionar_aluno(aluno2)

for aluno in turma_python.alunos:
   print(aluno)


# Exercicio 09
#Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" 
# e atributos de instância nome e idade. 
# Mostre a diferença entre acessar especie pelo objeto e pela classe.

class Cachorro:
   especie = "Canis Familiaris"
   def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
      
cachorro1 = Cachorro("Cofap", 5)
cachorro2 = Cachorro("Lux", 7)

print(cachorro1.nome)
print(cachorro2.nome)
print(cachorro1.idade)
print(cachorro2.idade)