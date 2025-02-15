
#Base de datos de usuarios y contraseñas

usuarios = {
    "admin" : "1234",
    "usuario1" : "abcd",
    "invitado": "guest"
}

#Máximo de intenos permitiso

intentos = 3

# bucle para validar el acceso
while intentos >0:
    usuario = input("Por favor, ingresa tu nombre de usuario: ")
    contraseña = input("Por favor, ingresa tu contraseña: ")

    #verificar si el usuario o contraseña son correctos
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"\n Bienvenido {usuario}, has iniciado sesión exitosamente. ")
        break
    else:
        intentos -= 1
        print(f"Nombre y/o usuario incorrecto. {intentos} intento(s) restantes")

if intentos == 0:
        print("\nAcceso Bloqueado. Intenta de nuevo más tarde. ")