#exercicio 01 criar uma lista de livros contendo 3 livros diferentes e exibir a lista na tela
books = ["Harry Potter", "A Volta ao mundo em 80 dias", "Lord of the rings"]
print(books)

#exercicio 02 usando a lista livros, exibir apenas o primeiro e o último elemento

print(books[0], books[-1])

#exercicio 03 adicionar dois livros a lista livros usando o metodo apped e xibir a lista atualizada

books.append("Star Wars")
books.append("Capitães de Areia")
##talvez quisesse adicionar os dois? seria books.append(["Star Wars", "Capitães de Areia"])
print(books)

#Exercicio 04 Inserir livro "Duna" na segunda posição da listra de livros usando insert()

books.insert(1,"Duna")
print(books)

#Exercicio 05 remover o livro "silencio dos inocentes" caso não exista, imprimir livro não encontrado


if "Silêncios dos Inocentes" in books:
    books.remove("Silêncio dos Inocentes")
else:
    print("Livro não encontrado")

#Exercicio 06 criar lista com valores 1,2,3,2,4,2,5. mostrar quantos números 2 aparece na lista

numeros =[1,2,3,2,4,2,5]
print(f"o número 2 aparecer {numeros.count(2)} vezes")

#Exericio 07 percorrer a lista livros e exibir cada livro com a frase "o livro <nome do livro> é interesante "

for book in books:
    print(f"O livro {book} é interessante!")

#Exercicio 08 dada a lista idades, usar um laço para exibir somente as idades maiores ou iguais a 18

ages = [12,18,25,14,30]

for age in ages:
    if age >= 18:
        print(age)

#Exercicio 09 criar uma lista de valores 10,20,30,40. usar um laço for para calcualr manualmente a soma de todos os valores

values =[10,20,30,40]
soma = 0
for value in values:
    soma += value
print(soma)

#Exercicio 10  Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em 
# uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = []
num_aluno = 0

print("---Digite 3 notas, para o primeiro aluno e depois mais 3 notas para o segundo aluno ---")

for contador_aluno in range(2):
    notas_deste_aluno = []
    for _ in range(3):
        notas_deste_aluno.append(float(input("Digita a nota ")))
        
        
    notas.append(notas_deste_aluno)

for lista_deste_aluno in notas:
    media = sum(lista_deste_aluno) / len(lista_deste_aluno)
    num_aluno +=1

    print(f" A média do aluno {num_aluno} é: {media:.2f}")