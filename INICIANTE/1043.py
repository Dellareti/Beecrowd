A,B,C = map(float,input().split())

if (A+B > C) and (B+C > A) and (A+C > B):
    print(f"Perimetro = {A+B+C}")
else:
    print(f"Area = {((A+B)*C)/2}")