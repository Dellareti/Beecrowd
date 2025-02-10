def salario (horas_trabalhadas,valor_hora):
    return (horas_trabalhadas * valor_hora)
    
number = int(input(""))
horas = int(input(""))
valor = float(input(""))

resultado_valor = salario(horas,valor)

print(f"NUMBER = {number}\nSALARY = U$ {resultado_valor:.2f}")