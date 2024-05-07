#12011EBIO18
#Vitória Dias Brito
#03-premio-milhao

dias = 0  #contador
soma = 0  #contador 
i = 1 #contador para as linhas de entrada
n = int(input()) #recebe um número inteiro (indica as linhas da entrada)

while (i<=n): #laço para as linhas de entrada
    acesso = int(input()) #pede os valores int de acessos
    soma = soma+ acesso #soma os valores de acesso 
    if (soma >= 1000000) and (dias == 0): #assim q a soma chegar a 1 mihão 
        dias = i          #recebe o valor de i (linha da entrada)
    i+=1        #contador continua o laço até n 
    
print(dias)  #imprime o valor de dias


#existem duas condições no if, uma para quando a soma atingir 1 milhao e a outra
#é para garantir q o valor impresso em dias se trata realmente do primeiro dia
#quando a soma foi alcançada, por isso (dias == 0)
