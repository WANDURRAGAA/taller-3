tabla = int(input("Ingrese un número: "))

while tabla == 0:
    tabla = int(input("Ingrese un número: "))

print("Tabla del", tabla)
for i in range(1, 11):
    print(tabla, "x", i, "=", tabla * i)
    
