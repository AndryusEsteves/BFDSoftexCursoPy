# Lista de Exercícios – POO: Classes e Objetos

# 1) ContaBancaria com saldo privado, getter e setter
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    # Getter
    def get_saldo(self):
        return self.__saldo

    # Setter (com regra de não aceitar saldo negativo)
    def set_saldo(self, valor):
        if valor < 0:
            print("Erro: o saldo não pode ser negativo!")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saque inválido!")

# Teste ContaBancaria
print("Exercício 1:")
conta = ContaBancaria("Andryus", 100)
print("Saldo inicial:", conta.get_saldo())

conta.depositar(50)
print("Após depósito:", conta.get_saldo())

conta.sacar(30)
print("Após saque:", conta.get_saldo())

conta.set_saldo(-500)  # tentativa inválida
print("Saldo final:", conta.get_saldo())
print("-" * 50)


# 2) Pessoa com cpf e identidade privados, getters e setters
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    # Getter e Setter para CPF
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        if len(str(novo_cpf)) == 11:  # regra simples de validação
            self.__cpf = novo_cpf
        else:
            print("Erro: CPF inválido!")

    # Getter e Setter para Identidade
    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, nova_identidade):
        if len(str(nova_identidade)) >= 5:  # regra simples
            self.__identidade = nova_identidade
        else:
            print("Erro: Identidade inválida!")

# Teste Pessoa
print("Exercício 2:")
pessoa = Pessoa("Maria", "01/01/1990", "12345678901", "RG12345")
print("Nome:", pessoa.nome)
print("Data de Nascimento:", pessoa.data_nascimento)
print("CPF:", pessoa.get_cpf())
print("Identidade:", pessoa.get_identidade())

pessoa.set_cpf("11122233344")
pessoa.set_identidade("RG67890")
print("Novo CPF:", pessoa.get_cpf())
print("Nova Identidade:", pessoa.get_identidade())
