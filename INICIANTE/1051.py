salario = float(input(""))
imposto_total = 0

if salario > 0 and salario <= 2000:
    print("Isento")
elif salario > 2000 and salario <= 3000:
    imposto_total = (salario - 2000) * 0.08
    print(f"R$ {imposto_total :.2F}")
elif salario > 3000 and salario <= 4500:
    imposto_total = (1000* 0.08) + ((salario - 3000) * 0.18)
    print(f"R$ {imposto_total :.2F}")
elif salario > 4500:
    imposto_total = (1000 * 0.08) + (1500 * 0.18) + ((salario - 4500) * 0.28)
    print(f"R$ {imposto_total :.2F}")
