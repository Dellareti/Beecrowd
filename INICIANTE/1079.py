n = int(input(""))  

valor_total = 0
media_ponderada = []

for i in range(n):
    A, B, C = map(float, input().split())
    valor_total = ((A * 2) + (B * 3) + (C * 5)) / 10
    media_ponderada.append(valor_total)

j = 0

while j < n:
    print(f"{media_ponderada[j]:.1f}")
    j += 1


