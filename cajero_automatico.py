# Declaración del inventario de billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10
# Declaración del inventario total que se tiene
billetes_total = (1000 * billetes_1000) + (500 * billetes_500) + (200 * billetes_200) + (100 * billetes_100) + (50 * billetes_50)

# Declaración de billetes a entregar
entregar_1000 = entregar_500 = entregar_200 = entregar_100 = entregar_50 = 0

# Inicio del sistema
print("\n --Bienvenid@ al cajero automático-- ")

# Creación del ciclo
while True:
    try:
        entrada = int(input(" Ingrese el monto a retirar: "))
        # Inicio de condiciones que se debe cumplir
        if entrada <= 0:
            print(" El monto debe ser mayor que 0.\n")
        elif entrada % 50 != 0:
            print(" La cantidad debe ser múltiplo de 50.\n")
        elif entrada > billetes_total:
            print(" No hay suficientes billetes disponibles.\n")
        else:
            # Monto válido, salir del ciclo while
            break

    except ValueError:
        print(" Debe ingresar un número válido.\n")

# Calcular billetes a entregar
cantidad_valida = entrada

for valor, entrega, inventario in [
    (1000, "entregar_1000", billetes_1000),
    (500, "entregar_500", billetes_500),
    (200, "entregar_200", billetes_200),
    (100, "entregar_100", billetes_100),
    (50, "entregar_50", billetes_50)
]:
    if cantidad_valida >= valor:
        necesarios = cantidad_valida // valor
        disposicion = min(necesarios, inventario)
        cantidad_valida -= disposicion * valor
        globals()[entrega] = disposicion  # Asigna dinámicamente el número de billetes entregados

#  Resultado
if cantidad_valida == 0:
    print("\n Retiro exitoso. Billetes entregados:")
    if entregar_1000: print(f" - {entregar_1000} billete(s) de $1000")
    if entregar_500: print(f" - {entregar_500} billete(s) de $500")
    if entregar_200: print(f" - {entregar_200} billete(s) de $200")
    if entregar_100: print(f" - {entregar_100} billete(s) de $100")
    if entregar_50: print(f" - {entregar_50} billete(s) de $50")

    # Actualizar inventario
    billetes_1000 -= entregar_1000
    billetes_500 -= entregar_500
    billetes_200 -= entregar_200
    billetes_100 -= entregar_100
    billetes_50 -= entregar_50

    print("\n Inventario actualizado:")
    print(f" 1000: {billetes_1000}\n"
          f" 500: {billetes_500}\n"
          f" 200: {billetes_200}\n"
          f" 100: {billetes_100}\n"
          f" 50: {billetes_50}")

