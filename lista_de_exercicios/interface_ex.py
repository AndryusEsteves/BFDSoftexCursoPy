#Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. 
# Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod

# Interface
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

# Classes que implementam a interface
class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R${valor:.2f} processado no cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R${valor:.2f} gerado via boleto bancário.")

# Exemplo de uso
cartao = CartaoCredito()
boleto = Boleto()

cartao.processar(250.00)
boleto.processar(400.00)


#Interface múltipla
# Crie duas interfaces: Ligavel (com o método ligar()) e 
# Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. 
# Mostre seu uso.

from abc import ABC, abstractmethod

# Interfaces
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

# Classe que implementa as duas interfaces
class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado.")

    def desligar(self):
        print("Computador desligado.")

# Exemplo de uso
pc = Computador()
pc.ligar()
pc.desligar()


#Interface em herança múltipla
#Crie uma interface Imprimivel com o método imprimir(). 
# Crie outra interface Exportavel com o método exportar(). 
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

from abc import ABC, abstractmethod

# Interfaces
class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass

# Classe que herda de ambas
class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("Relatório impresso em papel.")

    def exportar(self):
        print("Relatório exportado em PDF.")

# Exemplo de uso
rel = Relatorio()
rel.imprimir()
rel.exportar()


#Forçando contrato

#Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
# O que acontece quando você tenta instanciá-la? Corrija o código.

from abc import ABC, abstractmethod

# Interface
class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

# Classe que implementa parcialmente (gera erro se tentar instanciar)
class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

# Tentando instanciar causará erro:
# repo = RepositorioMemoria()  # ❌ TypeError: Can't instantiate abstract class ...

# Correção — implementando todos os métodos
class RepositorioMemoriaCorrigido(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        print(f"Objeto com ID {id} recuperado da memória.")

# Exemplo de uso
repo = RepositorioMemoriaCorrigido()
repo.salvar("Cliente01")
repo.buscar(101)


