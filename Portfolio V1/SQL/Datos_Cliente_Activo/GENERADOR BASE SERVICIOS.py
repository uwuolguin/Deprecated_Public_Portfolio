import psycopg2
import pandas as pd
import numpy as np
import psycopg2.extras as extras

conn = psycopg2.connect("dbname=cliente_activo user=postgres password=Cl0Udpopi")
cursor = conn.cursor()
postgreSQL_select_Query_VENTAS = "select * from base_ventas_cliente_activo"
cursor.execute(postgreSQL_select_Query_VENTAS)
VENTAS_records = cursor.fetchall()

df = pd.DataFrame.from_records(VENTAS_records, columns =['rut_servicio', 'fecha_servicio', 'vin_servicio','email_servicio','nombre_cliente_servicio','marca','concesionario_servicio'])
df['N_OT'] = range(1, len(df) + 1)
df['fecha_servicio'] = df['fecha_servicio'] + pd.DateOffset(months=6)
conn.close()

def execute_values(conn, df, table):
  
    tuples = [tuple(x) for x in df.to_numpy()]
  
    cols = ','.join(list(df.columns))
    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()


conn = psycopg2.connect(
    database="cliente_activo", user='postgres', password='Cl0Udpopi', host='localhost', port='5432'
)
  
  
execute_values(conn, df, 'base_servicios_cliente_activo')

