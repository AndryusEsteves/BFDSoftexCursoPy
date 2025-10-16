#Atividade: POO - Classes abstratas
#Definição de classe abstrata
#Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
# Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método.
# Mostre o uso criando objetos e chamando o método falar().

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def falar(self):
        pass
class Cachorro(Animal):
    def falar(self):
        print("Au au")
        pass
class Gato(Animal):
    def falar(self):
        print("Meow")
        pass

totoh = Cachorro()
totoh.falar()

lion = Gato()
lion.falar()

#Proibição de instanciamento
#Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

new_animal = Animal()

#new_animal = Animal()
#TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'falar'
#Can't instantiate: "Não é possível criar um objeto (instanciar)..."

#abstract class Animal: "...da classe abstrata Animal..."

#without an implementation for abstract method 'falar': ""
#"...sem uma implementação (um código real) para o método abstrato (a regra obrigatória) 'falar'."


#Múltiplos métodos abstratos
# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). 
# Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos.
# Teste criando um objeto e calculando sua área e perímetro.

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return  2 * (self.base + self.altura)

forma1 = Retangulo(10,5)
calculo = forma1.area()
calculo2 = forma1.perimetro()

print(f"A área do retângulo é: {calculo}")
print(f"O perímetro do retângulo é: {calculo2}")

#Herança parcial
#Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar().
#  Depois, crie uma subclasse Carro que implemente apenas o método mover(). 
# O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

        
from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O carro está em movimento.")

    def parar(self):
        print("O carro parou.")

meu_carro = Carro()
meu_carro.mover()
meu_carro.parar()
