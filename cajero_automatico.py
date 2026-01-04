# Declaración del inventario de billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10


# Función para calcular el inventario total
def inventario_total():
    return (1000 * billetes_1000) + (500 * billetes_500) + \
        (200 * billetes_200) + (100 * billetes_100) + (50 * billetes_50)


# Inicio del sistema
print("\n --Bienvenid@ al cajero automático-- ")

# CICLO PRINCIPAL → permite varios retiros
while True:

    # Verificar si el cajero aún tiene billetes
    if inventario_total() == 0:
        print("\n--- El cajero está sin fondos. Operación finalizada. ---")
        break

    print(f"\nFondos disponibles: ${inventario_total()}")

    # Creación del ciclo para validar la cantidad
    while True:
        try:
            entrada = int(input("Ingrese el monto a retirar: "))

            if entrada <= 0:
                print("El monto debe ser mayor que 0.\n")
            elif entrada % 50 != 0:
                print("La cantidad debe ser múltiplo de 50.\n")
            elif entrada > inventario_total():
                print("No hay suficientes billetes disponibles.\n")
            else:
                break

        except ValueError:
            print("Debe ingresar un número válido.\n")

    # Declaración de billetes a entregar
    entregar_1000 = entregar_500 = entregar_200 = entregar_100 = entregar_50 = 0
    cantidad_valida = entrada

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
            locals()[entrega] = disposicion

    # Resultado
    if cantidad_valida == 0:
        print("\nRetiro exitoso. Billetes entregados:")
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

        print("\nInventario actualizado:")
        print(f" 1000: {billetes_1000}")
        print(f" 500: {billetes_500}")
        print(f" 200: {billetes_200}")
        print(f" 100: {billetes_100}")
        print(f" 50: {billetes_50}")

    # Preguntar si desea continuar
    opcion = input("\n¿Desea realizar otro retiro? (s/n): ").strip().lower()
    if opcion != "s":
        print("\nGracias por utilizar el cajero. ¡Hasta pronto!")
        break

