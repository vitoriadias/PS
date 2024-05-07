jogador1 = input("Jogador 1, digite pedra, papel, tesoura, lagarto ou spock: ")
jogador2 = input("Jogador 2, digite pedra, papel ou tesoura, lagarto ou spock: ")

if (jogador1 == jogador2):
    print("Empate! Ninguém ganhou.") # empate
    
elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
     (jogador1 == "tesoura" and jogador2 == "papel") or \
     (jogador1 == "papel" and jogador2 == "pedra") or \
     (jogador1 == "spock" and jogador2 == "tesoura") or\
     (jogador1 == "spock" and jogador2 == "pedra") or\
     (jogador1 == "lagarto" and jogador2 == "spock") or\
     (jogador1 == "lagarto" and jogador2 == "papel") or\
     (jogador1 == "pedra" and jogador2 == "lagarto") or\
     (jogador1 == "papel" and jogador2 == "spock") or\
     (jogador1 == "tesoura" and jogador2 == "lagarto"):
     
    print("Jogador 1 ganhou.")
else:
    print("Jogador 2 ganhou.")
