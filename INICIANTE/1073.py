x = int(input(""))

dentro = 0 
fora = 0 

for i in range(x):
    num = int(input(""))

    if num >= 0 and num <=20:
        dentro+= 1
    else:
        fora+=1

print(f"{dentro} in")
print(f"{fora} out")