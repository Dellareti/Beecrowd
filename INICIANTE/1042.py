A,B,C = map(int,input().split())

lista = [A,B,C]

numerosOrdenados = sorted(lista)

for elemento in numerosOrdenados:
    print(elemento)

print(f"\n{A}\n{B}\n{C}")