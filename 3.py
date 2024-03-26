piezas = 0
n = int(input("ingrese el numero de piezas:"))

while n > 0:
    longitud = float(input("Ingresa la longitud de la pieza:"))
    if 1.20 <= longitud <= 1.30:
        piezas += 1
    n -= 1
print("El numero de piezas aptas en el lote:", piezas)