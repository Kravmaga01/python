import re


def listarDatos(estudiantes):
    print("\n Estudiantes: \n")
    contador = 1
    for cur in estudiantes:
        datos= "{0}. codigo: {1} | nombre : {2} apellido: {3} edad: {4} | Curso: {5}  estado: {6}"
        print(datos.format(contador, cur[0], cur[1], cur[2], cur[3], cur[4], cur[5]))
        print(" ")
def perdirDatosRegistro():
    nombre = input("Ingreso nombre:\n ")
    apellido =input("Ingreso apellidos:\n ")
    edad = int(input("Ingresa edad:\n"))
    curso = input("Ingreso curso:\n")
    estado = input("Ingrese estado:\n")
    estudiantes = (nombre,apellido,edad,curso,estado)
    return estudiantes
def pedirDatosEliminacion(estudiantes):
    listarDatos(estudiantes)
    exitesCodigo = False
    codigoEliminar = int(input("ingrese el id del estudiante a eliminar:\n"))
    for estu in estudiantes:
        if estu[0] == codigoEliminar:
            exitesCodigo = True
            break
    
    if not exitesCodigo:
        codigoEliminar = ""
    

    return codigoEliminar



