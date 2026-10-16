# leer_csv.R — Cargar el reporte CSV del ERP (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_csv.R

# TODO 1: carga data/ventas.csv con readr::read_csv en un data.frame
# TODO 2: imprime las dimensiones (dim) del data.frame
# TODO 3: imprime las primeras filas (head) para revisar las columnas
library(readr)
ventas <- read_csv(
    "C:\\Users\\USUARIO\\Desktop\\Universidad-EPN\\4 TO SEMESTRE\\Estadistica I\\Labo1\\IDSD422-lab1-lectura-datos\\data\\ventas.csv")
head(ventas)
dim(ventas)
str(ventas) 
