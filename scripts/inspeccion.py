# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total


import pandas as pd

# TODO 1: Cargar data/ventas.csv
ventas = pd.read_csv("C:\\Users\\USUARIO\\Desktop\\Universidad-EPN\\4 TO SEMESTRE\\Estadistica I\\Labo1\\IDSD422-lab1-lectura-datos\\data\\ventas.csv")

# TODO 2: Imprimir la estructura y tipos de datos
print("\n--- ESTRUCTURA Y TIPOS DE DATOS ---")
print(ventas.dtypes)

print("\n--- TIPO DE DATO DE REGION ---")
print(ventas["region"].dtype)

# TODO 3: Crear la columna ticket = ventas / clientes
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]

print("\n--- PRIMERAS FILAS CON TICKET ---")
print(ventas.head())

# TODO 4: Calcular e imprimir resultados

# Venta promedio por sucursal
print("\n--- VENTA PROMEDIO POR SUCURSAL ---")
venta_promedio = ventas.groupby("sucursal")["ventas"].mean()
print(venta_promedio)
venta_promedio_general = ventas["ventas"].mean()
print(venta_promedio_general)

# Ticket promedio (ventas totales / clientes totales)
print("\n--- TICKET PROMEDIO GENERAL ---")
ticket_promedio = ventas["ventas"].sum() / ventas["clientes"].sum()
print(ticket_promedio)

# Ventas totales por sucursal
ventas_sucursal = ventas.groupby("sucursal")["ventas"].sum()

# Sucursal con mayor venta total
print("\n--- SUCURSAL CON MAYOR VENTA TOTAL ---")
mayor = ventas_sucursal.idxmax()
print(ventas_sucursal.loc[[mayor]])

# Sucursal con menor venta total
print("\n--- SUCURSAL CON MENOR VENTA TOTAL ---")
menor = ventas_sucursal.idxmin()
print(ventas_sucursal.loc[[menor]])

# Región con mayor venta total
ventas_region = ventas.groupby("region")["ventas"].sum()

print("\n--- REGION CON MAYOR VENTA TOTAL ---")
mayor_region = ventas_region.idxmax()
print(ventas_region.loc[[mayor_region]])

