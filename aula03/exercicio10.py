print("---- Calculando o troco ----")
compra = float( input("Informe o valor da compra: ") )
pagamento = float( input("Informe o valor do pagamento: ") )
troco = float(pagamento-compra)
print("--- Realizando cálculo ---")

if pagamento > compra : 
    print("O troco é de R$: ", troco )
else:
    print("Você está devendo pague: ", -troco)