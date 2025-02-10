HoraInicical,HoraFInal = map(int,input().split())

diferenca = (HoraFInal -HoraInicical)

if diferenca <= 0:
    diferenca = diferenca + 24
    print(f"O JOGO DUROU {diferenca} HORA(S)")
else:
    print(f"O JOGO DUROU {diferenca} HORA(S)")