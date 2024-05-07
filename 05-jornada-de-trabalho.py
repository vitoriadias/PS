#Vitória Dias Brito 12011EBI018
#05-jornada-de-trabalho

def imprime(diaria,extra,salario): #função que imprime a saida 
    print(f"Horas trabalhadas: {diaria}") #saida horas trabalhadas
    print(f"Horas extras: {extra}")         #saidas horas extras
    print(f"Valor devido: R$ {salario:.2f}") #saida salario

def main():     #função principal
    v = int(input())    #valor a hora
    d = int(input())    #dias trabalhados
    i = 0       #contador     
    extra1 = 0  #variavel p hora extra diaria
    extra2 = 0  #variavel p hora extra semanal
    diaria = 0  #variavel p horas trabalhadas por dia
    while(i<d):     #laço 1 : varia ao passo que dias mudam, vai até d
        qnt = int(input()) #quantidade de periodos
        j = 0        
        while(j<qnt):   #laço 2: varia ao passo que os peridos mudam, vai até qnt
            inicio = int(input()) #inicio do periodo
            fim = int(input())      #fim do periodo
            horadia = (fim - inicio) #horas trabalhadas no periodo
            diaria = diaria + horadia #horas do dia, soma pra cada periodo
            if (horadia>8): #condição q verifica se tem hora extra diaria
                extra1 = extra1 + (horadia - 8)
            j = j+1 #contador laço 2
        i = i+1 #contador laço 1
    if((diaria - extra1)>44): #condição q verifica se tem hora extra semanal
        extra2 = extra2 + ((diaria - extra1) - 44)

    if ((extra2 != 0) and (extra1 !=0)): #condição q verifica as horas extras
        extra = extra2 #se as duas nao forem vazias, só considera o extra2
        salario = (v*diaria)+((v/2)*extra)#calcula o salario
    else:
        extra = extra2 + extra1
        salario = (v*diaria)+((v/2)*extra)

    imprime(diaria,extra,salario) #chama a funçao


main()
