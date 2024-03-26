contraseña = "marito"

while True:
    digito = input("Ingrese la contraseña:")
    if digito == contraseña:
        print("Acceso concendido")
        break
    else:
        print("Siga intentando")