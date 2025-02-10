seg = int(input(""))

horas = seg // 3600
seg = seg % 3600

minutos = seg // 60
seg = seg % 60

print(f"{horas}:{minutos}:{seg}")