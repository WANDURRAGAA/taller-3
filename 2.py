n = int(input("Ingrese la cantidad de trabajadores: "))

contador = 1
total = 0

while contador <= n:
    horas_trabajadas = float(input(f"Ingrese las horas trabajadas para el trabajador {contador}: "))
    tarifa_hora = float(input(f"Ingrese la tarifa por hora para el trabajador {contador}: "))

    salario = horas_trabajadas * tarifa_hora
    total += salario

    contador += 1

print(f"El salario total del grupo de trabajadores es: {total}")