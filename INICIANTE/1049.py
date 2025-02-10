inv = input("")
classe = input("")
comida = input("")

if inv == "vertebrado":
    if classe == "ave":
        if comida == "carnivoro":
            print("aguia")
        else:
           print("pomba")
    else:
        if comida == "onivoro":
            print("homem")    
        else:
            print("vaca")
else:
    if classe == "inseto":
        if comida == "hematofago":
            print("pulga")
        else:
           print("lagarta")
    else:
        if comida == "hematofago":
            print("sanguessuga")    
        else:
            print("minhoca")