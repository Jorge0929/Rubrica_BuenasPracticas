#se importa flash y pyocbc
from flask import Flask
import pyodbc
#abrir conexion base de datos y el cursor
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ= C:\Users\jorge\OneDrive\Documentos\base\TallerDB.accdb;")
cursor=conn.cursor()

lista=[]
#se define una funcion en el cual se recorren las filas y añaden los valores a la lista
def añadiralist():
    for row in cursor.fetchall():
        lista.append(row)

#se ejecutan la consultas y guardan los valores en variables
cursor.execute("SELECT * FROM Estudiantes")
añadiralist()
Estudiantes=lista

cursor.execute("SELECT * FROM cursos")
añadiralist()
cursos=lista

#se crea una app en flash
app = Flask(__name__)

#se define la ruta
@app.route('/')
def index():
    return f"<h2>Esta es la tabla de estudiantes</h2> <br> {Estudiantes} <br> <h2>Esta es la tabla de cursos</h2> <br>{cursos}"

if __name__=='__main__':
    app.run()

#cerrar la conexion y el cursor
cursor.close()
conn.close()