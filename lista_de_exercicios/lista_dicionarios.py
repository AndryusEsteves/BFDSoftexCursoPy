#LISTA DE EXERCICIOS SOBRE DICIONÁRIOS

#EXERCICIO 1

#Crie um dicionário simples

#    Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.

aluno = {"nome": "Andryus", "idade": 39, "nota": 5.0}

#EXERCICIO 2

# Acessando valores

# Dado o dicionário:

# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

# Imprima o nome do produto e a quantidade em estoque.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

print(produto["nome"], produto["estoque"])

#EXERCICIO 3
# Adicionando novos pares chave-valor

#     Dado o dicionário:

#     pessoa = {"nome": "Carlos", "idade": 30}

#     Adicione uma nova chave "cidade" com valor "São Paulo"

pessoa ={"nome": "carlos", "idade": 30}
pessoa["cidade"] = "São Paulo"
print(pessoa)

#EXERCICIO 4

# Removendo elementos

#     Dado o dicionário:

#     carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}

#     Remova a chave "ano" do dicionário.

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"] 
print(carro)

#EXERCICIO 5

# Verificando existência de uma chave

#     Verifique se a chave "telefone" existe no dicionário:

#     contato = {"nome": "Ana", "email": "ana@email.com"}

contato = {"nome": "Ana", "email": "ana@email.com"}

if "telefone" in contato:
    print(f"O item existe no dicionário")
else:
    print(f"o item não existe no dicionário")

#EXERCICIO 6

# Contando frequência de palavras

#     Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

#    palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

def  contar_frequencia(palavras):
    repetidas = {}
    for palavra in palavras:
        if palavra in repetidas:
            repetidas[palavra] +=1
        else:
            repetidas[palavra] = 1
    return repetidas

dicionario = contar_frequencia(palavras)
print(dicionario)

# EXERCICIO 7

# Invertendo um dicionário

#     Dado o dicionário:

#     d = {"a": 1, "b": 2, "c": 3}

#     Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}

d ={"a": 1, "b":2, "c": 3}
resultado ={}

for chave in d:
    resultado[d[chave]] = chave

print(resultado) 

# EXERCICIO 8

# Dicionário com listas
# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.

alunos = {"Andryus": [5,6,9], "Kleber": [2,5,7], "Fredinho": [9,8,7] }

for aluno in alunos:
    media = sum(alunos[aluno]) / len(alunos[aluno])
    print(f"A  média de {aluno} é {media:.2f}") 


#EXERCICIO 9

# Mesclando dois dicionários

# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. 
# Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
    
dicionario_1 = {"nome": "Kleber", "idade": 39, "genero": "masculino", "Tipo_sanguineo": "O+"}
dicionario_2 = {"nome": "Carla", "idade": 25, "genero": "feminino"}

def mescla_dic(dicionario_1,dicionario_2):

    resultado = dicionario_1.copy()
    resultado.update(dicionario_2)
    return resultado

dicionario = mescla_dic(dicionario_1, dicionario_2)
print (dicionario)

#EXERCICIO 10

# Ordenando dicionário por valor

#     Dado o dicionário:

#     pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

#     Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

ordenados = sorted(pontuacoes.items(), key=lambda par: par[1], reverse = True)

for nome, pontuacao in ordenados:
    
    print(f"{nome}:{pontuacao}")