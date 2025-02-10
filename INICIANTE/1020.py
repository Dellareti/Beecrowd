idade_dias = int(input(""))

print(f"{idade_dias//365} ano(s)")
idade_dias = idade_dias % 365

print(f"{idade_dias//30} mes(es)")
idade_dias = idade_dias % 30

print(f"{idade_dias} dia(s)")
