# leer_excel.R — Cargar el consolidado Excel de finanzas (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/leer_excel.R

# TODO 1: carga data/ventas.xlsx con readxl::read_excel indicando la hoja
# TODO 2: imprime las dimensiones (dim) y las primeras filas (head)
install.packages("readxl")
library(readxl)
ventas <- read_excel("C:\\Users\\USUARIO\\Desktop\\Universidad-EPN\\4 TO SEMESTRE\\Estadistica I\\Labo1\\IDSD422-lab1-lectura-datos\\data\\ventas.xlsx", sheet = "ventas")
head(ventas)
dim(ventas)
str(ventas)