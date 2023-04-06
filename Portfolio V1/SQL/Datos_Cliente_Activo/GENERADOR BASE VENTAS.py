import names
import random
import string
from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


RecolectorVIN=[]
Marca=["OPEL","NISSAN","CHEVROLET","TOYOTA","KIA"]
Concesionarios=["DERCO","SUZUVAL","EKOVACS","BRUNOFRITSH","WBM MOTORS"]
inicio=datetime. strptime('1/1/2008',"%m/%d/%Y")
final=datetime. strptime('12/31/2022',"%m/%d/%Y")

L=["create table BASE_VENTAS_CLIENTE_ACTIVO ( \n RUT_VENTA VARCHAR(50),\n FECHA_VENTA DATE,\n VIN_VENTA VARCHAR(50),\n EMAIL_VENTA VARCHAR(50),\n NOMBRE_CLIENTE_VENTA VARCHAR(50), \n MARCA VARCHAR(50), \n CONCESIONARIO VARCHAR(50));\n \n"]


for i in range(1000):
    Rut=get_random_string(10)
    Vin=get_random_string(17)
    RecolectorVIN.append(Vin)
    fecha=random_date(inicio,final)
    fechaVenta= fecha.strftime("%m/%d/%Y")
    Nombre=names.get_full_name()
    Mail =Nombre.replace(" ","")+"@gmail.com"
    Marca_u=random.choice(Marca)
    Concesionario=random.choice(Concesionarios)
    L.append("insert into BASE_VENTAS_CLIENTE_ACTIVO (RUT_VENTA, FECHA_VENTA, VIN_VENTA, EMAIL_VENTA, NOMBRE_CLIENTE_VENTA, MARCA, CONCESIONARIO) values ('{}','{}','{}','{}','{}','{}','{}');\n".format(Rut,fechaVenta,Vin,Mail,Nombre,Marca_u,Concesionario))



plan_peranciones = open("BASE_VENTAS.sql","w")
plan_peranciones.writelines(L)
plan_peranciones.close()