#Lista de Exercícios: Função lambda (map, filter, reduce, sorted)
#  Dobro dos números (map + lambda)
#  Dada a lista [1, 2, 3, 4, 5], 
# use map com lambda para gerar uma nova lista com o dobro de cada número.

lista = [1, 2, 3, 4, 5 ]
lista1 = map(lambda num: num*2, lista)
print(list(lista1))

# Filtrar pares (filter + lambda)
# Dada a lista [10, 15, 20, 25, 30] 
# use filter com lambda para obter apenas os números pares.

lista = [10, 15, 20, 25, 30]
filtro = filter(lambda num : num % 2 == 0, lista)
print(list(filtro))

# Soma dos números (reduce + lambda)
# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5]

from functools import reduce
lista = [1, 2, 3, 4, 5]
reduzida = reduce(lambda x, y: x + y, lista)
print(reduzida)

# Ordenação por comprimento da palavra (sorted + lambda)
# Dada a lista ["uva", "banana", "maçã", "laranja"], 
# ordene as palavras pelo tamanho usando sorted e lambda.

lista = ["uva", "banana", "maçã", "laranja"]
por_comprimento = sorted(lista, key=lambda palavra: len(palavra))
print(por_comprimento)

# Primeira letra maiúscula (map + lambda)
# Dada a lista ["ana", "pedro", "maria"], 
# use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

lista = ["ana", "pedro", "maria", "carlos", "roberto"]
Upper = map(lambda nome: nome.capitalize(), lista)
print(list(Upper))

# Produto dos números (reduce + lambda)
# Usando reduce, calcule o produto (multiplicação) de todos os elementos 
# da lista [2, 3, 4, 5].

from functools import reduce

lista = [2, 3, 4, 5]

reducao = reduce(lambda x, y : x * y, lista)

print(reducao)

# Ordenar por último caractere (sorted + lambda)
# Dada a lista ["banana", "uva", "maçã", "laranja"], 
# ordene as palavras pelo último caractere.

lista = ["banana", "uva", "maçã", "laranja"]

ord_carac = sorted(lista, key=lambda x: x[-1])

print(ord_carac)

