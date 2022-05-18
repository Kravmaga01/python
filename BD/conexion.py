from distutils.log import error
from sqlite3 import Cursor
from typing_extensions import Self
import mysql.connector
from  mysql.connector import Error

class DAO(): 
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='Matriculas'
                )
        except   Error as ex:
            print(f"Error al conectar: {ex}");
    def listarDatos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM estudiantes ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"Error al intentar la conexión: {ex}")
    
    def registarEstudiante(self, estudiantes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql ="INSERT INTO  estudiantes (id,nombre,apellido,edad,curso, estado) values('{0}','{1}','{2}','{3}','{4}','{5}')"
                cursor.execute(sql.format(estudiantes[0],estudiantes[1],estudiantes[2],estudiantes[3],estudiantes[4],estudiantes[5]))
                self.conexion.commit()
                print("Estudiante registrado\n")
            except:
                print("Error al intentar la conexión ")  