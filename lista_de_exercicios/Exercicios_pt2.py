#Exercicio 11 Usando list comprehension, crie um tabuleiro de xadrez vazio e depois 
# adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, 
# identifique as posições do tabuleiro da seguinte forma:
#
#    [ ] - para posições vazias
#    tor - para a torre
#    cav - para o cavalo
#    bis - para o bispo
#    rai - para a rainha
#    rei - para o rei
#    pea - para o peão

# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra.
#  (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)


tabuleiro = [["[  ]"for _ in range(8)] for _ in range(8) ]
for coluna in range(8):
    tabuleiro[6][coluna] = "peaB"
    tabuleiro[1][coluna] = "peaP"

tabuleiro[7] = ["torB", "cavB", "bisB", "raiB", "reiB", "bisB", "cavB", "torB"]
tabuleiro[0] = ["torP", "cavP", "bisP", "raiP", "reiP", "bisP", "cavP", "torP"]

for linha in tabuleiro:
    print(" ".join(linha))

