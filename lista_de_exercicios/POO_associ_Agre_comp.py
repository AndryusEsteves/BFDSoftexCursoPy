# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles

class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.livro_atual = None
        pass
    def possuir(self, posse):
        self.livro_atual = posse
        pass
    def ler(self):
        if self.livro_atual:
            print(f"{self.nome} está lendo o livro: {self.livro_atual.titulo}")
        else:
            print(f"{self.nome} não tem nenhum livro para ler.")
        pass
class Livro():
    def __init__(self, titulo):
        self.titulo = titulo
        pass

carlos = Pessoa("Carlos")
livro1 = Livro("O alquimista")
carlos.possuir(livro1)
carlos.ler()

#Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Aluno():
    def __init__(self,nome, passagem):
        self.nome = nome
        self.passagem = passagem
    def pegar_onibus(self, onibus):
       if self.passagem == True:
        print(f"{self.nome} pegou o onibus e vai para o destino {onibus.destino}")
       else:
        print(f"O aluno {self.nome} não possui passagem")
        pass
class Onibus():
    def __init__(self, numero, destino):
        self.numero = numero
        self.destino = destino
        pass

aluno1 = Aluno("Rogerio", False)
aluno2 = Aluno("José", True)
bus1 = Onibus("243", "Marco Zero")
aluno1.pegar_onibus(bus1)
aluno2.pegar_onibus(bus1)

#Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.

class Funcionario():
    def __init__(self,nome,cargo):
        self.nome = nome
        self.cargo = cargo
class Departamento():
    def __init__(self, dpt_nome):
        self.dpt_nome = dpt_nome
        self.funcionarios = []
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        
f1 = Funcionario("Ana", "Tech Leader")
f2 = Funcionario("Sandra", "UX-Design")
dp_ti = Departamento("TI")
dp_ti.adicionar_funcionario(f1)
dp_ti.adicionar_funcionario(f2)

print(len(dp_ti.funcionarios))


# Crie as classes Time e Jogador. 
# Um Jogador tem nome e posição como atributos, 
# enquanto Time agrega jogadores em uma lista.


class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome} - {self.posicao}"


class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  # lista para armazenar os jogadores

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        print(f"Time: {self.nome}")
        for jogador in self.jogadores:
            print(jogador)


# Exemplo de uso
if __name__ == "__main__":
    time = Time("Flamengo")
    jogador1 = Jogador("Pedro", "Atacante")
    jogador2 = Jogador("Arrascaeta", "Meia")

    time.adicionar_jogador(jogador1)
    time.adicionar_jogador(jogador2)

    time.listar_jogadores()


#Crie a classe Carro que possui um Motor.
#O Motor deve ser criado dentro do Carro. 
# Se o Carro deixar de existir, o Motor também deixa. 
# Mostre isso criando e depois apagando o objeto.

class Motor:
    def __init__(self):
        print("Motor criado.")

    def __del__(self):
        print("Motor destruído.")


class Carro:
    def __init__(self):
        self.motor = Motor()
        print("Carro criado.")

    def __del__(self):
        print("Carro destruído.")


# Criando o carro (e automaticamente o motor)
carro = Carro()

# Apagando o objeto carro
del carro

# Força o Python a executar o coletor de lixo imediatamente
import gc
gc.collect()


#Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). 
# Cada Comodo deve ser criado dentro da Casa.

class Comodo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Cômodo '{self.nome}' criado.")

    def __del__(self):
        print(f"Cômodo '{self.nome}' destruído.")


class Casa:
    def __init__(self):
        # Criação dos cômodos dentro da casa (composição)
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]
        print("Casa criada.")

    def __del__(self):
        print("Casa destruída.")


# Criando a casa (e automaticamente os cômodos)
casa = Casa()

# Apagando o objeto casa
del casa

# Força o coletor de lixo a executar imediatamente
import gc
gc.collect()

