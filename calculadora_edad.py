# Se importa la librería datetime para trabajar con fechas
import datetime


# Se crea la función calculadora, aquí se realizará el cálculo de la edad
def calculadora():
    # Ciclo que se repetirá hasta que el usuario ingrese datos válidos
    while True:
        fecha_str = input("Introduce tu fecha de nacimiento (DD-MM-AAAA): ")
        try:
            # Convertir la cadena el objeto date
            fecha_nacimiento = datetime.datetime.strptime(fecha_str, "%d-%m-%Y").date()

            # Validaciones para cada parte de la fecha de nacimiento

            # Día debe estar entre 1 y 31
            if fecha_nacimiento.day > 31 or fecha_nacimiento.day < 1:
                print("Dato del día inválido")

            # Mes debe estar entre 1 y 12
            elif fecha_nacimiento.month > 12 or fecha_nacimiento.month < 1:
                print("Dato del mes inválido")

            # Año mínimo permitido (evita fechas imposibles o demasiado antiguas)
            elif fecha_nacimiento.year < 1900:
                print("Dato del año inválido")

            else:
                # Si todos los datos son válidos, se rompe el ciclo
                break

        # Si el usuario introduce un valor no numérico
        except ValueError:
            print("Ingresa datos válidos")

    # Cálculo de la edad:
    # Se toma el año actual y se resta el año de nacimiento.
    # Luego se ajusta la edad restando 1 si todavía no llega el cumpleaños este año.
    edad = (
            datetime.datetime.now().year
            - fecha_nacimiento.year
            - (
                    (datetime.datetime.now().month, datetime.datetime.now().day)
                    < (fecha_nacimiento.month, fecha_nacimiento.day)
            )
    )

    # Se imprime la edad calculada
    print(f"Tu edad es: {edad}")


# Se manda a llamar a la función para ejecutar el programa
calculadora()
