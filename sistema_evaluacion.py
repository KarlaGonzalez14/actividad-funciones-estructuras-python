# Se crean las funciones que se utilizaran para el sistema de evaluación
# Las siguientes funciones validan texto y números sujetas a diferentes condiciones

def pedir_texto(mensaje):
    while True:  # Repetir hasta tener texto válido
        valor = input(mensaje).strip()  # Se elimina espacios
        if not valor:  # Si quedó vacío
            print("Este campo no puede quedar vacío. Intenta de nuevo.")
        else:
            return valor  # Si tiene contenido, se devuelve


def pedir_numero(mensaje):
    while True:  # Ciclo para repetir hasta que el usuario ingrese un valor válido
        valor = input(mensaje).strip()  # Se pide el dato y se eliminan espacios
        if not valor:  # Validación: campo vacío
            print("Este campo no puede quedar vacío. Intenta de nuevo.")
            continue  # Vuelve a pedir el dato
        if not valor.isdigit():  # Validación: solo deben ser números enteros
            print("Debes ingresar un número válido.")
            continue
        return int(valor)  # Se convierte a entero y se regresa


def pedir_calificacion(materia):
    while True:  # Ciclo para validar calificación
        valor = input(f"Calificación de {materia}: ").strip()
        if not valor:  # Validación: vacío
            print("La calificación no puede quedar vacía.")
            continue
        try:
            cal = float(valor)  # Convertimos a número decimal
            if 0 <= cal <= 10:  # Validamos el rango permitido
                return cal
            else:
                print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Debes ingresar un número válido.")  # Si no es número



print("--- SISTEMA DE EVALUACIÓN DE ALUMNOS ---")  # Inicio del sistema

# Se pide cuántos alumnos se van a registrar
num_alumnos = pedir_numero("¿Cuántos alumnos deseas registrar?: ")

# Se pide cuántas materias tiene cada alumno
num_materias = pedir_numero("¿Cuántas materias tiene cada alumno?: ")

materias = []  # Lista vacía para guardar los nombres de las materias

print("\n--- Registro de Materias ---")
for i in range(num_materias):  # Se repite según el número de materias
    nombre_materia = pedir_texto(f"Nombre de la materia {i+1}: ")  # Pide el nombre
    materias.append(nombre_materia)  # Agrega la materia a la lista

alumnos = []  # Lista para almacenar la información completa de cada alumno

print("\n--- Registro de Alumnos ---")
for i in range(num_alumnos):  # Repetir por cada alumno
    print(f"\n--- Alumno {i+1} ---")  # Encabezado
    nombre = pedir_texto("Nombre del alumno: ")  # Nombre del alumno
    matricula = pedir_texto("Matrícula del alumno: ")  # Matrícula del alumno

    calificaciones = {}  # Diccionario para guardar calificaciones por materia

    for materia in materias:  # Se pide calificación para cada materia
        cal = pedir_calificacion(materia)  # Función que valida calificación
        calificaciones[materia] = cal  # Guardamos materia: calificación

    # Se agrega la estructura con toda la info del alumno a la lista
    alumnos.append({
        "nombre": nombre,
        "matricula": matricula,
        "calificaciones": calificaciones
    })


# Evaluar aprobados, reprobados y promedio general

print("\n--- RESULTADOS ---")
for alumno in alumnos:
    print(f"\nAlumno: {alumno['nombre']} - Matrícula: {alumno['matricula']}")

    total = 0  # Suma de calificaciones
    for materia, cal in alumno["calificaciones"].items():
        estado = "APROBADO" if cal >= 6 else "REPROBADO"
        print(f"  {materia}: {cal} --> {estado}")
        total += cal

    # Calcular promedio general
    promedio = total / num_materias

    # Evaluar estado general
    estado_general = "APROBADO" if promedio >= 6 else "REPROBADO"

    print(f"\nPromedio general: {promedio:.2f} --> {estado_general}")

