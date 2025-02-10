import math

def formula_bhaskara ():
    A, B,C  = map (float,input().split())

    if A == 0:
        print(f"Impossivel calcular")
        return 

    delta = ((B * B) - (4 * A * C))

    if (delta <= 0):
        print(f"Impossivel calcular")
    else:
        R1 = ((-B + math.sqrt(delta)) / (2*A))
        R2 = ((-B - math.sqrt(delta)) / (2*A))
        print(f"R1 = {R1:.5f}")
        print(f"R2 = {R2:.5f}")

formula_bhaskara ()

