# listas

# lista =[]
# print(type(lista))

frutas =["lemon", "banana", "morango", "coconut"]
#print(frutas)


### adicionando elementos
#frutas.insert(1, "apple") # vai inserir a maçã no lugar da banana, e desloca a lista
#print(frutas)
#frutas.append("kiwi")
#print(frutas)

frutas_vermelhas = ["morango", "amora", "uva" ]

frutas+=frutas_vermelhas # adiciona uma lista a outra (frutas_Vermelhas a frutas)
#print(frutas)

#### Removendo itens
print("Removendo elementos")
print(frutas.count("morango"))
frutas.remove("morango")
print(frutas)

print("primeiro pop")
frutas.pop()
print(frutas)

print("segundo pop")
frutas.pop(4)
print(frutas)

del frutas [2] #deleta a variavel (se não informar o index) ou o endereço na lista
print(frutas)

### copia de lista

frutas2 = frutas[:]
frutas2 = frutas.copy()
print(frutas2)
print(id(frutas))
print(id(frutas2))