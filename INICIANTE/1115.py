x,y = map(int,input().split())

while (x != 0 and y != 0):
    if x > 0 and y > 0:
        print("primeiro")
    elif x > 0 and y < 0:
        print("quarto")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    x,y = map(int,input().split())
