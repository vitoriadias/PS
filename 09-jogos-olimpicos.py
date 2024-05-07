#Vitória Dias Brito
#09-jogos-olimpicos

def pedeprovas(lista1): #pede cada prova e os paises respectivos
    
    quadromed = [] #cria uma matriz com o quadro de medalhas
    for i in range(lista1[0]): #de acordo com o numero de provas pede as linhas
        entrada2 = input()
        provas = entrada2.split()
        linha = [str(valor) for valor in provas]
        quadromed.append(linha)

    calculamedalha(quadromed,lista1)

def calculamedalha(quadromed,lista1):
    paisouro = 0
    #paisprata = 0
    #paisbronze = 0

    for i in range(len(quadromed)):
        for j range(quadromed[0]):
            paisouro = quadromed[i][1]
            #paisprata = quadromed[i][2]
            #paisbronze = quadromed[i][3]
            
    

def main():

    entrada1 = input() #entrada dos valores de peso
    m = entrada1.split()
    lista1 = [int(valor) for valor in m] #cria lista com os elementos    
    saida = pedeprovas(lista1)
    print(saida)

main()
