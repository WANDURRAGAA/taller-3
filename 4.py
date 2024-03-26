empleados = int(input("Ingrese el numero de empleados:"))
n100_300 = 0
n_300 = 0
total = 0

while empleados > 0:
    salario = float(input("Ingrese el salario del empleado:"))
    total += salario
    if salario >= 100 and salario <= 300:
        n100_300 += 1
    elif salario > 300:
        n_300 += 1
    empleados -= 1
print("El numero de empleados que cobran entre 100 y 300 son:" , n100_300)
print("El numero de empleados que cobran mas de 300 son:", n_300)
print("El total de gasto de la compañia en salarios son:", total)