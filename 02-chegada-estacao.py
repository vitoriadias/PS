#12011EBI018
#Vitória Dias Brito
#02-chegada-estacao

x = int(input()) #distância em km entre as duas estações (valor inteiro)
t = int(input()) #diferença em min do tempo de saída dos dois trens (valor inteiro)
v_1 = float(input()) #velocidade do trem T1 em km/h (valor real)
v_2 = float(input()) # velocidade do trem T2 em km/h (valor real)

tempo1 = (x*60)/v_1 #calcula o tempo q T1 leva p percorrer o percurso (regra de 3)
tempo2 = ((x*60)/v_2)+t #calcula o tempo de T2 e soma a diferença de minutos
if(tempo1<tempo2): #compara os dois tempos, se T1 for menor, vdd. 
    print (True)
else:               #caso contrário, falso
    print (False)
