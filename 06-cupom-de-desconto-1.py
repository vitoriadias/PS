#Vitória Dias Brito
#12011EBI018
#06-cupom-de-desconto-1

def calculadesconto(x1,z1,x2,z2,x3,z3):
    compras = []
    cupom1 = 0
    cupom2 = 0
    cupom3 = 0
    desconto1 = 0
    desconto2 = 0
    desconto3 = 0
    comprai = 0
    comprak = 0
    compraj = 0
    igual = 0
    igual2 = 0
    n = int(input())
    for i in range(n):
        valorcompra = int(input())
        compras.append(valorcompra)
    
    
    for i in range(len(compras)):        
        if (compras[i]>z1):
            if(igual2!=i) and (igual!=i):
                if (compras[i]>desconto1):
                    desconto1 = compras[i]
                    cupom1 = x1
                    comprai = i + 1
            
        for j in range(len(compras)):
            if(igual!=j):
                desconto2 = (compras[j]*x2)/100
                if (desconto2>z2):
                    desconto2 = z2
                elif (desconto2>cupom2):
                        cupom2 = desconto2
                        compraj = j+1
                        igual2 = j
                
            for k in range(len(compras)):
                if (compras[k]>z3):
                    desconto3 = (compras[k]*x3)/100
                    if (desconto3>cupom3):
                        cupom3 = desconto3
                        comprak = k+1
                        igual = k
    print(comprai)                    
    print(compraj)
    print(comprak)



def main():
    x1 = int(input())
    z1 = int(input())
    x2 = int(input())
    z2 = int(input())
    x3 = int(input())
    z3 = int(input())
    calculadesconto(x1,z1,x2,z2,x3,z3)
    


main()
