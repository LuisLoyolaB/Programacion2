import mysql.connector,os
from mysql.connector.errors import Error
os.system("cls")

try:
    conectar = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database ='boliche'
    )
    if conectar.is_connected():
        print("Conexión Exitosa!!!")
        #Cursor
        cursor = conectar.cursor()
        # Datos
        cod = int(input("Ingresa código : "))
        det = input("Ingresa Detalle: ")
        pre= int(input("Ingresa Precio: "))
        sql = "INSERT INTO producto(codigo,detalle,precio) values (%s,%s,%s)"
        # Crear Cursor
        cursor.execute(sql,(cod,det,pre))
        conectar.commit() # Confirmar la acción
        print("\n Registro Ingresado \n ")
except Error as e:
    print(f"error en la conexión : {e}")

finally:
    if conectar.is_connected():
        conectar.close()
        print("Conexión Finalizada") 