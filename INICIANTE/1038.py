codigo, quantidade = map(int, input().split())

if (codigo == 1):
    print(f"Total: R$ {(quantidade * 4):.2f}")
    
elif (codigo == 2):
    print(f"Total: R$ {(quantidade * 4.5):.2f}")
    
elif (codigo == 3):
    print(f"Total: R$ {(quantidade * 5):.2f}")
    
elif (codigo == 4):
    print(f"Total: R$ {(quantidade * 2):.2f}")

elif (codigo == 5):
    print(f"Total: R$ {(quantidade * 1.5):.2f}")

else:
    print(f"digite um valor válido")

