m, n = map(int, input().split())

while m > 0 and n > 0:
    # Garantir que n seja sempre o menor e m o maior
    if m > n:
        m, n = n, m
    
    sum = 0
    lista = []
    
    # Somar do menor (m) até o maior (n)
    for i in range(m, n + 1):
        sum += i
        lista.append(i)
    
    # Converter a lista de inteiros para uma lista de strings antes de usar join()
    print(f"{' '.join(map(str, lista))} Sum={sum}")
    
    m, n = map(int, input().split())
