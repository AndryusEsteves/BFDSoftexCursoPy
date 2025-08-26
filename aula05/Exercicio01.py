## exercicio01
lista = ["macaco", 1 , 2.0, "banana", [1,2,4]]
print(lista)

lista.append(5)
print(lista)

## exercio02
lista[4].insert(2,3)
print(lista)

lista.remove(5)
print(lista)

##exercicio03
lista2 = lista.copy()
print(id(lista))
print(id(lista2))