victory_rosa = 0
lose_rosa = 0
draw = 0

for game_number in range(1,6):

    gols_rosa = int(input("Quantos gols o Rosariense marcou?: "))
    gols_adve = int(input("Quantos gols marcou o time adversário?: "))
    print(f"Gols da Seleção no jogo {game_number}: {gols_rosa} ") 
    print(f"Gols do adversário no jogo {game_number}: {gols_adve} ")
    
    if gols_rosa > gols_adve:
        victory_rosa +=1
    elif gols_rosa < gols_adve:
        lose_rosa +=1
    else:
        draw +=1        

print(f"=== Torneio de futebol === \nVitórias: {victory_rosa} \nEmpates: {draw} \nDerrotas: {lose_rosa}")
   