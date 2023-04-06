from tableauhyperapi import HyperProcess, Telemetry, Connection, CreateMode, NOT_NULLABLE, NULLABLE, \
SqlType, TableDefinition, Inserter, escape_name, escape_string_literal, HyperException, TableName

import tableauserverclient as TSC
import pandas as pd
import psycopg2

#########Tableau#####################
tableau_auth = TSC.PersonalAccessTokenAuth('uwu96', 'Z7ip8aXtTkOOsW1x6hK3VQ==:pDzK0qHrO4m7PfJ36C7olcvJoYjIOhP0', 'bulls')
server = TSC.Server('https://10ax.online.tableau.com/', use_server_version=True)
server.auth.sign_in(tableau_auth)

######Conexion y a  .hyper ####################

conn = psycopg2.connect("dbname=cliente_activo user=postgres password=Cl0Udpopi")
cursor = conn.cursor()
postgreSQL_select_Query_VENTAS = "select * from base_ventas_cliente_activo"
postgreSQL_select_Query_SERVICIOS = "select * from base_servicios_cliente_activo"
cursor.execute(postgreSQL_select_Query_VENTAS)
VENTAS_records = cursor.fetchall()
cursor.execute(postgreSQL_select_Query_SERVICIOS)
SERVICIOS_records = cursor.fetchall()

df_servicios = pd.DataFrame.from_records(SERVICIOS_records, columns =['rut_servicio', 'fecha_servicio', 'vin_servicio','email_servicio','nombre_cliente_servicio','marca','concesionario_servicio','n_ot'])
df_ventas= pd.DataFrame.from_records(VENTAS_records, columns =['rut_venta', 'fecha_venta', 'vin_venta','email_venta','nombre_cliente_venta','marca','concesionario'])

with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU) as hyper:

    with Connection(hyper.endpoint, 'Servicios.hyper', CreateMode.CREATE_AND_REPLACE) as connection:

        connection.catalog.create_schema('Extract')
        
        example_table = TableDefinition(TableName('Extract','Servicios'), [
            TableDefinition.Column('rut_servicio', SqlType.varchar(500)),
            TableDefinition.Column('fecha_servicio', SqlType.date()),
            TableDefinition.Column('vin_servicio', SqlType.varchar(500)),
            TableDefinition.Column('email_servicio', SqlType.varchar(500)),
            TableDefinition.Column('nombre_cliente_servicio', SqlType.varchar(500)),
            TableDefinition.Column('marca', SqlType.varchar(500)),
            TableDefinition.Column('concesionario_servicio', SqlType.varchar(500)),
            TableDefinition.Column('n_ot', SqlType.varchar(500)),

         ])

        connection.catalog.create_table(example_table)
        with Inserter(connection, example_table) as inserter:
            for i in range(0,len(df_servicios.index)):
                row_list = df_servicios.loc[i, :].values.flatten().tolist()
                inserter.add_row(
                    row_list
            )
            inserter.execute()
            
            
    with Connection(hyper.endpoint, 'Ventas.hyper', CreateMode.CREATE_AND_REPLACE) as connection:

        connection.catalog.create_schema('Extract')
        
        example_table2 = TableDefinition(TableName('Extract','Ventas'), [
            TableDefinition.Column('rut_venta', SqlType.varchar(500)),
            TableDefinition.Column('fecha_venta', SqlType.date()),
            TableDefinition.Column('vin_venta', SqlType.varchar(500)),
            TableDefinition.Column('email_venta', SqlType.varchar(500)),
            TableDefinition.Column('nombre_cliente_venta', SqlType.varchar(500)),
            TableDefinition.Column('marca', SqlType.varchar(500)),
            TableDefinition.Column('concesionario', SqlType.varchar(500)),

         ])

        connection.catalog.create_table(example_table2)
        with Inserter(connection, example_table2) as inserter:
            for i in range(0,len(df_ventas.index)):
                row_list = df_ventas.loc[i, :].values.flatten().tolist()
                inserter.add_row(
                    row_list
            )
            inserter.execute()
conn.close()

project_id = 'b191a1dd-2c5d-4483-8f62-3ef308ad0fc3'

file_path_s = "c:/Users/acos2/OneDrive/Desktop/A_TEAM/Tableau developing/Cliente Activo/Servicios.hyper"

file_path_v = "c:/Users/acos2/OneDrive/Desktop/A_TEAM/Tableau developing/Cliente Activo/Ventas.hyper"

servicios_datasource = TSC.DatasourceItem(project_id,'servicios')

ventas_datasource = TSC.DatasourceItem(project_id,'ventas')

server.datasources.publish(servicios_datasource, file_path_s, 'Overwrite')

server.datasources.publish(ventas_datasource, file_path_v, 'Overwrite')

