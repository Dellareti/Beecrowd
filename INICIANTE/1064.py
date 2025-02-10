number = 0

def ispositive():
    global number  # Declarar que number é uma variável global
    positivo = 0
    for i in range(6):
        num = float(input(""))

        if num > 0:
            positivo += 1
            number += num  # Somar os números corretamente
    
    print(f"{positivo} valores positivos")
    print(f"{number/positivo :.1f}")

ispositive()
