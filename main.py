import opcode
from sqlite3 import Cursor
from BD.conexion import DAO
import funciones
from mysql.connector import Error


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("===============Menú pricipal=============\n")
            print("1.Listar estudiante\n")
            print("2.Listar  registar estudainte\n")
            print("3.Listar  actualizar estudiante\n")
            print("4.Listar eliminar estudiante\n")
            print("5.salir")
            print("==========================\n")
            opcion = int(input("seleciones la opción:\n"))

            if opcion < 1 or opcion > 5:
                print("Opcion incorrecta, ingrese el valor nuevamente\n")
            elif opcion == 5:
                continuar = False
                print("Gracias por usar este sistema\n")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            estudiantes = dao.listarDatos()

            if len(estudiantes) > 0:
                funciones.listarDatos(estudiantes)
            else:
                print("no se encontraron datos")
        except Error as ex:
            print(f"Ocurrio un error {ex}")
        print("listar")
    elif opcion == 2:
        estudiantes = funciones.perdirDatosRegistro()
        try:
            dao.registarEstudiante(estudiantes)
        except Error as ex:
            print(f"Ocurrio un error {ex}")
    elif opcion == 3:
        try:
            estudiantes = dao.listarDatos()
            if len(estudiantes)>0:
                estudiantes = funciones.pedeirDatosActualizacion(estudiantes)
                if estudiantes:
                    dao.actualizarEstudiante(estudiantes)
                else:
                    print(f"codigo de estudiantate a actualizar no encontrado: {estudiantes}")
        except Error as ex:
            print(f"Error al intentar eliminar {ex}")    
    elif opcion == 4:
        try:
            estudiantes = dao.listarDatos()
            if len(estudiantes)>0:
                codigoEliminar= funciones.pedirDatosEliminacion(estudiantes)
                if not(codigoEliminar == ""):
                    dao.eliminarEstudiante(codigoEliminar)
        except Error as ex:
            print(f"Error al intentar eliminar {ex}")
    else:
        print("opción no valida")


menuPrincipal()
