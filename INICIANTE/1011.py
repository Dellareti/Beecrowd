def volume_esfera(raio):
    return ((4/3) * 3.14159 * raio ** 3)

r = float(input(""))
resultado = volume_esfera(r)

print(f"VOLUME = {resultado:.3f}")
    