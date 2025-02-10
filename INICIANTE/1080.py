maior = 0 
posicao = 0

for i in range(100):
    numero = int(input(""))
    if numero > maior:
        maior = numero
        posicao = i+1

print(f"{maior}\n{posicao}")