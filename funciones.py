def listarDatos(estudiantes):
    print("\n Estudiantes: \n")
    contador = 1
    for cur in estudiantes:
        datos= "{0}. codigo: {1} | nombre : {2} apellido: {3} edad: {4} | Curso: {5}  estado: {6}"
        print(datos.format(contador, cur[0], cur[1], cur[2], cur[3], cur[4], cur[5]))
        print(" ")
def perdirDatosRegistro():
    Id = input("Ingreso cóndigo:\n ")
    nombre = input("Ingreso nombre:\n ")
    apellido =input("Ingreso apellidos:\n ")
    edad = int(input("Ingresa edad:\n"))
    curso = input("Ingreso curso\n")
    estado = input("Ingrese estado\n")
    estudiante = (Id,nombre,apellido,edad,curso,estado)
    return estudiante