def omaior():
    a, b, c = map(int, input().split())
    
    maiorAB = ((a+b + abs(a-b)) )/2
    maiorMC = (maiorAB + c + abs(maiorAB -c))/2
    print(f"{maiorMC:.0f} eh o maior")

omaior()