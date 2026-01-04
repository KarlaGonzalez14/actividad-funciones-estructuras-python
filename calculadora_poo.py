class Calculadora:
    """Clase calculadora con historial y operaciones básicas."""

    # Método constructor: inicializa los atributos de la calculadora
    def __init__(self, numero1=0, numero2=0):
        self._numero1 = numero1   # Primer número de la operación
        self._numero2 = numero2   # Segundo número de la operación
        self._historial = []      # Lista donde se guardarán las operaciones realizadas

    """--------- SETTER Y GETTER ----------"""
    @property
    def numero1(self):
        """Devuelve el valor del primer número."""
        return self._numero1

    @numero1.setter
    def numero1(self, nuevo_numero1):
        """Asigna un nuevo valor al número 1 validando que sea numérico."""
        if isinstance(nuevo_numero1, (int, float)):
            self._numero1 = nuevo_numero1
        else:
            raise ValueError("numero1 debe ser int o float")

    @property
    def numero2(self):
        """Devuelve el valor del segundo número."""
        return self._numero2

    @numero2.setter
    def numero2(self, nuevo_numero2):
        """Asigna un nuevo valor al número 2 validando que sea numérico."""
        if isinstance(nuevo_numero2, (int, float)):
            self._numero2 = nuevo_numero2
        else:
            raise ValueError("numero2 debe ser int o float")

    """--------- OPERACIONES ----------"""

    def sumar(self):
        """Realiza la operación de suma."""
        resultado = self._numero1 + self._numero2
        self._registrar_operacion('+', resultado)
        return resultado

    def restar(self):
        """Realiza la operación de resta."""
        resultado = self._numero1 - self._numero2
        self._registrar_operacion('-', resultado)
        return resultado

    def multiplicar(self):
        """Realiza la operación de multiplicación."""
        resultado = self._numero1 * self._numero2
        self._registrar_operacion('*', resultado)
        return resultado

    def dividir(self):
        """Realiza la división verificando que no sea entre cero."""
        if self._numero2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        resultado = self._numero1 / self._numero2
        self._registrar_operacion('/', resultado)
        return resultado

    """--------- HISTORIAL ----------"""

    def _registrar_operacion(self, operador, resultado):
        """Guarda la operación realizada en el historial."""
        self._historial.append({
            'operacion': f"{self._numero1} {operador} {self._numero2}",
            'resultado': resultado
        })

    def ver_historial(self):
        """Muestra todas las operaciones realizadas."""
        if not self._historial:
            print("No hay operaciones en el historial.")
            return

        print("\n--- Historial de Operaciones ---")
        for i, operacion in enumerate(self._historial, start=1):
            print(f"{i}. {operacion['operacion']} = {operacion['resultado']}")

"""
Función para interpretar expresiones como:
'5 + 5', '10 / 2', '3 * 4'
Devuelve: número1, número2 y operador
"""
def interpretar_expresion(expresion: str):
    """Procesa la expresión matemática ingresada por el usuario."""
    expresion = expresion.strip()

    # Lista de operadores que la calculadora puede interpretar
    for operador in ['+', '-', '*', '/']:
        if operador in expresion:
            partes = expresion.split(operador)

            # Se valida que tenga exactamente un operador
            if len(partes) == 2:
                try:
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                    return num1, num2, operador
                except ValueError:
                    return None
    return None


"""--------- FUNCIÓN PRINCIPAL ----------"""
def main():
    calc = Calculadora()  # Se crea un objeto de la clase Calculadora
    print("Calculadora básica. Escribe 'salir' para terminar o 'historial' para ver operaciones.\n")

    while True:
        entrada = input("Ingresa la operación (ejemplo: 5 + 5): ")

        # Opción para salir
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break

        # Opción para mostrar historial
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue

        # Procesa la expresión ingresada
        resultado = interpretar_expresion(entrada)

        # Valida si la expresión es correcta
        if not resultado:
            print("Expresión no válida. Usa el formato: número operador número.\n")
            continue

        num1, num2, operador = resultado
        calc.numero1 = num1
        calc.numero2 = num2

        # Ejecuta la operación correspondiente
        try:
            if operador == '+':
                print("Resultado:", calc.sumar())
            elif operador == '-':
                print("Resultado:", calc.restar())
            elif operador == '*':
                print("Resultado:", calc.multiplicar())
            elif operador == '/':
                print("Resultado:", calc.dividir())
        except Exception as e:
            print("Error:", e)


# Ejecuta la calculadora
if __name__ == "__main__":
    main()
