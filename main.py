# Importación de librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.colors import *

# 📌 Cargar los datos desde un archivo CSV
df = pd.read_csv('data/Financial Sample.csv')

# 📌 Limpieza de nombres de columnas (eliminación de espacios adicionales)
columnas = []
for column in df.columns:
    columnas.append(column.strip())
df.columns = columnas

# 📌 Reemplazo de valores vacíos en las columnas numéricas
for col in df.columns:
    df[col] = df[col].replace(" $-\u2007\u2007 ", "0")

# 📌 Conversión de columnas numéricas a formato flotante
columnas_numericas = ["Units Sold", "Manufacturing Price", "Sale Price", "Gross Sales", "Discounts", "Sales", "COGS",
                      "Profit"]
df[columnas_numericas] = df[columnas_numericas].replace('[\$,)]', '', regex=True)
df[columnas_numericas] = df[columnas_numericas].replace('[(]', '-', regex = True).astype('float')


# 📌 Cálculo de métricas financieras por país
ventas_brutas_por_pais = df.groupby("Country")["Gross Sales"].sum().round(0)
ventas_brutas_por_pais.name = "Ventas Brutas (€)"

promedio_ventas = df.groupby("Country")["Gross Sales"].mean().round(0)
promedio_ventas.name = "Promedio Ventas (€)"

total_profit = df.groupby("Country")["Profit"].sum().round(0)
total_profit.name = "Ganancias totales (€)"

# 📌 Cálculo del margen de ganancia
df["Profit_margin"] = df["Profit"] / df["Gross Sales"]
margen_ganancia_medio_por_pais = df.groupby("Country")["Profit_margin"].mean().round(6) * 100
margen_ganancia_medio_por_pais.name = "Margen de ganancia medio (%)"

# 📌 Cálculo de ingresos y ganancias totales por país
df['Ingresos'] = df['Sale Price'] * df['Units Sold']
ingresos_totales_por_pais = df.groupby('Country')['Ingresos'].sum().round(0)
ingresos_totales_por_pais.name = "Ingresos totales (€)"

ganancias_totales_por_pais = df.groupby('Country')['Profit'].mean().round(0)
ganancias_totales_por_pais.name = "Ganancias totales (€)"

# 📌 Creación de un DataFrame con las métricas calculadas
df_datos = pd.DataFrame(data=[ventas_brutas_por_pais, promedio_ventas, total_profit, margen_ganancia_medio_por_pais, ingresos_totales_por_pais, ganancias_totales_por_pais])
df_datos.columns = ["Canada", "France", "Germany", "Mexico", "USA"]

# 📌 Creación de la tabla en formato lista de listas
lista_filas = [["Estadísticas", "Canada", "France", "Germany", "Mexico", "USA"]]
lista_filas_data = df_datos.values.tolist()

# 📌 Redondeo de los valores de margen de ganancia medio
for i, value in enumerate(lista_filas_data[3]):
    lista_filas_data[3][i] = round(value, 2)

# 📌 Agregar nombres de filas a la tabla
nombre_filas = df_datos.index.tolist()
for index_fila, lista in enumerate(lista_filas_data):
    base = [nombre_filas[index_fila]]
    base.extend(lista)
    lista_filas.append(base)

# 📌 Configuración de la tabla en `reportlab`
tabla = Table(lista_filas, colWidths=[200, 70, 70, 70, 70], rowHeights=[35, 25, 25, 25, 25, 25, 25])

# 📌 Aplicación de estilos a la tabla
estilos = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), brown),
    ("GRID", (0, 0), (-1, -1), 1, black),
    ("TEXTCOLOR", (0, 0), (-1, 0), white),
    ("ALINGMENT", (0, 0), (-1, -1), "CENTER"),
    ("FONTSIZE", (0, 0), (-1, 0), 15),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
])
tabla.setStyle(estilos)

# 📌 Generación de gráficos con `matplotlib`
df_datos_values = df_datos.values.tolist()

# 📊 Gráfico de barras: Comparación de ganancias brutas y beneficios
plt.bar(df_datos.columns, df_datos_values[0], width=0.5)
plt.bar(df_datos.columns, df_datos_values[2], width=0.5)
plt.xlabel("Paises")
plt.ylabel("Valor (10.000.000 €)")
plt.legend(["Ganancias brutas", "Beneficios"])
plt.title("Comparacion entre ganancias brutas y beneficios")
plt.savefig("output/Barras_Ganancias_Beneficios")
plt.clf()

# 📊 Gráfico de dispersión (scatter) entre ganancias brutas y beneficios
color = ["red", "green", "yellow", "purple", "blue"]
paises = ["Canada", "France", "Germany", "Mexico", "USA"]
plt.scatter(df_datos_values[0], df_datos_values[2], c=color)
plt.xlabel("Ganancias brutas")
plt.ylabel("Beneficios")
for col, pais in zip(color, paises):
    plt.scatter([], [], color=col, label=pais)
plt.legend(title="Países")
plt.title("Scatter entre ganancias brutas y beneficios")
plt.savefig("output/Scatter_Ganancias_Beneficios")
plt.clf()

# 📊 Gráfico de pastel: Margen de ganancia medio por país
explode = [0.1, 0.1, 0.1, 0.1, 0.1]
labels_str = [f"{round(label, 2)}%" for label in df_datos_values[3]]
plt.pie(df_datos_values[3], labels=labels_str, explode=explode, startangle=20)
plt.legend(paises, loc="upper center")
plt.savefig("output/pie_Ganancias_Beneficios")
plt.clf()

# 📊 Gráfico de barras: Beneficios por país
plt.bar(df_datos.columns, df_datos_values[2], width=0.5)
plt.title("Beneficios por pais")
plt.ylabel("Beneficios (Millones de euros)")
plt.xlabel("Paises")
plt.savefig("output/Barras_Beneficios")
plt.clf()

# 📌 Creación del PDF con `reportlab`
from reportlab.lib.pagesizes import A4
c = canvas.Canvas("output/reporte_final.pdf", pagesize=A4)
width, height = A4

# 📄 Página 1: Título, tabla y gráfico de barras
c.setFont("Helvetica-Bold", 20)
c.drawCentredString(width/2, height - 50, "Reporte de Financial Sample")
c.setFont("Helvetica-Bold", 15)
c.drawCentredString(y = height - 80, x = width/2, text = "Autor: Victor Brown Sogorb")
c.setFont("Helvetica", 13)
c.drawString(40, height - 130, "Tabla informativa del reporte:")
tabla.wrapOn(c, 1000, 1000)
tabla.drawOn(c, 25, 500)
c.drawString(y = height -390, x = 40, text = "Gráficas informativas de los datos:")
c.drawString(y = height - 420, x = 40, text = "Beneficios por país:")
c.drawImage("output/Barras_Beneficios.png", x = 50, y = 30, height = 360, width = 480) #480,640
c.drawString(y = 10, x = width - 20, text = "1")
c.drawImage("data/7145.jpg", x = 30, y = height - 110, height = 100, width = 100)
c.showPage()

# 📄 Página 2: Más gráficos
c.drawString(y = height - 50, x = 40, text = "Ganancias brutas y beneficios por país:")
c.drawImage("output/Barras_Ganancias_Beneficios.png", x = 50, y = 430, height = 360, width = 480)
c.drawString(y = height - 450, x = 40, text = "Margen de ganancia por país:")
c.drawImage("output/pie_Ganancias_Beneficios.png", x = 50, y = 0, height = 360, width = 480)
c.drawString(y = 10, x = width - 20, text = "2")
c.showPage()
# # 📄 Página 3: Más gráficos
c.drawString(y = height - 50, x = 40, text = "Scatter entre ganancias brutas y beneficios:")
c.drawImage("output/Scatter_Ganancias_Beneficios.png", x = 50, y = 430, height = 360, width = 480)
c.drawString(y = 10, x = width - 20, text = "3")
c.save()

print(f"Pdf de reporte creado correctamente en {c._filename}")