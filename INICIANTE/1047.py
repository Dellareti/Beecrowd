HoraInicial,MinInicial,HoraFinal,MinFinal = map(int,input().split())

diferenca = ((HoraFinal * 60)+ MinFinal) - ((HoraInicial * 60)+ MinInicial)

if (diferenca <= 0):
    diferenca = diferenca + 24*60
    
hora = diferenca // 60
minuto = diferenca % 60
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")