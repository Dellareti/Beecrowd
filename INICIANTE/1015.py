import math

def distancia_entre_dois_pontos():
    
    entrada1 = input().split() 
    x1 = float(entrada1[0])
    y1 = float(entrada1[1])
    
    entrada2 = input().split() 
    x2 = float(entrada2[0])
    y2 = float(entrada2[1])
    
    resultado =  math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    print(f"{resultado:.4f}")

distancia_entre_dois_pontos() 