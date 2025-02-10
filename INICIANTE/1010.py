def calculo_simples(num_1, val_1, num_2, val_2):
    return ((num_1 * val_1) + (num_2 * val_2))

# Ler a primeira linha de entrada
entrada1 = input().split()
c1 = int(entrada1[0])
n1 = int(entrada1[1])
p1 = float(entrada1[2])

# Ler a segunda linha de entrada
entrada2 = input().split()
c2 = int(entrada2[0])
n2 = int(entrada2[1])
p2 = float(entrada2[2])

resultado = calculo_simples(n1, p1, n2, p2)

print(f"VALOR A PAGAR: R$ {resultado:.2f}")
