
somatoria = 0

while True:
    numero = int(input("Digite um número: "))
    somatoria += numero
    if numero == 0:
        print(somatoria)
        break