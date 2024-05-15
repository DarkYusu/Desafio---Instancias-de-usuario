from usuario import Usuario

# Función para manejar las excepciones y escribir en el archivo error.log
def manejar_excepcion(excepcion):
    with open("error.log", "a") as archivo_error:
        archivo_error.write(str(excepcion) + "\n")

# Abrir el archivo usuarios.txt en modo lectura
with open("usuarios.txt", "r") as archivo_usuarios:
    # Iterar sobre cada línea del archivo
    for linea in archivo_usuarios:
        try:
            # Convertir la línea JSON a un diccionario
            datos_usuario = eval(linea)
            
            # Crear una instancia de Usuario con los datos del diccionario
            usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"], datos_usuario["email"], datos_usuario["genero"])
            
            # Imprimir los detalles del usuario
            print(f"Usuario creado: {usuario.nombre} {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")
        
        except Exception as e:
            # Manejar la excepción escribiendo en el archivo error.log
            manejar_excepcion(e)
