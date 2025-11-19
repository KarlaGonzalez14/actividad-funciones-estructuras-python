# Credenciales válidas
usuario_correcto = "admin"
clave_correcta = "1234"

# Inicio del sistema
print("\n-- Sistema de inicio de sesión --")

# Número máximo de intentos
intentos = 3

# Ciclo de intentos
while intentos > 0:
    usuario = input("\nUsuario: ")
    clave = input("Contraseña: ")

    # Validar campos vacíos
    if usuario == "" or clave == "":
        print("\n-- ¡Error de autenticación! --\nDebe ingresar usuario y contraseña.")
    # Validar credenciales
    elif usuario == usuario_correcto and clave == clave_correcta:
        print("\n Bienvenido admin")
        break
    # Error de credenciales incorrectas
    else:
        intentos -= 1
        print("\n-- ¡Error! --\nLos datos ingresados son erróneos. Intente de nuevo.")
        print(f"Intentos restantes: {intentos}")

    # Mensaje final si ya no hay intentos
    if intentos == 0:
        print("\n Inténtelo más tarde, ha superado los intentos permitidos.")
