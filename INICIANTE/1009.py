def salario_bonus (sal_fixo,mon_vendas):
    return sal_fixo + (mon_vendas * 0.15)

nome = input("")
salario_fixo = float(input(""))
vendas = float(input(""))

resultado = salario_bonus(salario_fixo,vendas)

print(f"TOTAL = R$ {resultado:.2f}")
