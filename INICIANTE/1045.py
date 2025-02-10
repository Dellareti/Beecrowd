L1,L2,L3 = map(float,input().split())

lista = [L1,L2,L3]
lista.sort(key=float, reverse=True)

A = lista[0]
B = lista[1]
C = lista[2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")

elif (A ** 2) == (B ** 2) + (C ** 2):
    print("TRIANGULO RETANGULO")

elif (A ** 2) > (B ** 2) + (C ** 2):
    print("TRIANGULO OBTUSANGULO")
    if A == B or B == C or A == C :
        print("TRIANGULO ISOSCELES")
    else:
        ...
        
elif (A ** 2) < (B ** 2) + (C ** 2):
    print("TRIANGULO ACUTANGULO")
    if A == B and B == C and C == A:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C :
        print("TRIANGULO ISOSCELES")
    else:
        ...
   
        
