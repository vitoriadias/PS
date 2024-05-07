#Vitória Dias Brito
#12011EBI018
#01-combustivel

horas = int(input()) #entrada em inteiro
velocidade = int(input())  #entrada em inteiro

distancia = horas * velocidade #calculo da distancia percorrida
x = distancia/12 #calculo de quantos litros foi usado - regra de 3
print(f"{x:.3f}") #saida com apenas 3 casas depois da virgula
