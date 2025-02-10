salario = float(input(""))

reajuste = 0
percentual = 0

if 0 < salario <= 400:
    reajuste = salario * 0.15
    percentual = 15
elif 400 < salario <= 800:
    reajuste = salario * 0.12
    percentual = 12
elif 800 < salario <= 1200:
    reajuste = salario * 0.10
    percentual = 10
elif 1200 < salario <= 2000:
    reajuste = salario * 0.07
    percentual = 7
elif salario > 2000:
    reajuste = salario * 0.04
    percentual = 4

novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
