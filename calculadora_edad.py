# Se importa la librería datetime para trabajar con fechas
import datetime


# Se crea la función calculadora, aquí se realizará el cálculo de la edad
def calculadora():
    # Ciclo que se repetirá hasta que el usuario ingrese datos válidos
    while True:
        try:
            # Declaración de variables donde el usuario ingresa su fecha de nacimiento
            dia_nacimiento = int(input("Introduce tu día de nacimiento: "))
            mes_nacimiento = int(input("Introduce tu mes de nacimiento: "))
            ano_nacimiento = int(input("Introduce tu año de nacimiento: "))

            # Validaciones para cada parte de la fecha de nacimiento

            # Día debe estar entre 1 y 31
            if dia_nacimiento > 31 or dia_nacimiento < 1:
                print("Dato del día inválido")

            # Mes debe estar entre 1 y 12
            elif mes_nacimiento > 12 or mes_nacimiento < 1:
                print("Dato del mes inválido")

            # Año mínimo permitido (evita fechas imposibles o demasiado antiguas)
            elif ano_nacimiento < 1900:
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
            - ano_nacimiento
            - (
                    (datetime.datetime.now().month, datetime.datetime.now().day)
                    < (mes_nacimiento, dia_nacimiento)
            )
    )

    # Se imprime la edad calculada
    print(f"Tu edad es: {edad}")


# Se manda a llamar a la función para ejecutar el programa
calculadora()
