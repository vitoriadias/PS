#Vitória Dias Brito 12011EBI018
#04-magic-the-gathering

        
def contacartas(cartas,d,x,b):  #função q confere as cartas
    i = 1   #contadores
    cor = 0
    verdepreto = 0
    while(i<=cartas):   #enquanto nao tiver atingido o numero de cartas possiveis, continua a entrada
        cor = int(input())
        if (cor==5) or (cor==3):    #se for preto ou verde conta
            verdepreto = verdepreto+1
            if (verdepreto == d):   #quando o valor chegar em d, para de receber 
                break
        i = i+1
    if(i>=cartas):  #condição q confere se a quantidade de cartas compradas foram o max possivel com o dinheiro
        gasto = cartas*b #calcula gasto
        comprados = cartas
    else:
        gasto = i*b
        comprados = i
    
    restante = x-gasto
    print(f"ORCAMENTO: {x} REAIS")  #printa todas as saidas 
    print(f"VALOR DO BOOSTER: {b} REAIS")
    print(f"TOTAL GASTO: {gasto:.2f} REAIS")
    print(f"TOTAL RESTANTE: {restante:.2f} REAIS")
    print(f"QUANTIDADE DE BOOSTERS COMPRADOS: {comprados:.0f}")
    print(f"QUANTIDADE DESEJADA DE CARTAS DA COR VERDE OU DA COR PRETA: {d}")
     

    
    return verdepreto   #retorna o valor de cartas verdes e pretas alcançado 
    
def main():
    x = float(input())  #orçamento
    b = float(input())  #valor do booster
    d = int(input())    #quantidade de cartas verde ou preta
    cartas = x//b        #quantidade de cartas possíveis para compra
    qnt = contacartas(cartas,d,x,b) #chama a funçao passando 4 parametros
    print(f"QUANTIDADE OBTIDA DE CARTAS DA COR VERDE OU DA COR PRETA: {qnt}")

   
    
    if (qnt<d): #condição que verifica se conseuiu ou nao 
        print("JOAO NAO CONSEGUIU MONTAR SEU NOVO DECK!")
    else:
        print("JOAO CONSEGUIU MONTAR SEU NOVO DECK!")

main()  #chama a função principal  
