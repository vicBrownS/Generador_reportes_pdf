# **📊 Generador de Reportes en PDF a partir de Datos Financieros**  

### **📌 Descripción**
Este proyecto toma un conjunto de datos financieros desde un archivo CSV y genera un **reporte en PDF** que incluye:  
✔ **Procesamiento de datos con `pandas`**  
✔ **Gráficos de análisis con `matplotlib`**  
✔ **Generación de PDF con `reportlab`**  

El informe incluye métricas clave como ventas brutas, márgenes de ganancia y beneficios, además de gráficos visuales que ayudan a analizar los datos de manera efectiva.  

---

## **📂 Estructura del Proyecto**
```
📦 Proyecto
│-- 📜 main.py                  # Script principal para generar el reporte
│-- 📜 notebook_ejecucion.ipynb  # Jupyter Notebook con la ejecución del proceso
│-- 📂 data                      # Contiene los archivos de entrada
│   ├── Financial Sample.csv     # Datos financieros en formato CSV
│   ├── logo.png                 # Imagen del logotipo usada en el PDF
│-- 📂 output                    # Almacena los gráficos generados y el PDF final
│   ├── Barras_Ganancias_Beneficios.png
│   ├── Scatter_Ganancias_Beneficios.png
│   ├── Pie_Ganancias_Beneficios.png
│   ├── Barras_Beneficios.png
│   ├── reporte_final.pdf        # Documento final generado
│-- 📜 README.md                 # Documentación del proyecto
```

---

## **📦 Instalación**
Antes de ejecutar el proyecto, asegúrate de tener Python 3 y las siguientes librerías instaladas. Puedes hacerlo con:
```bash
pip install pandas matplotlib reportlab
```

---

## **🚀 Uso**
### **📌 1. Ejecutar el script principal**
Corre el archivo `main.py` desde la terminal o línea de comandos:
```bash
python main.py
```
Esto generará los gráficos y el **reporte en PDF** en la carpeta `output/`.

### **📌 2. Ejecutar desde Jupyter Notebook**
Si prefieres una ejecución paso a paso, abre `notebook_ejecucion.ipynb` en Jupyter y ejecuta cada celda.

---

## **📊 ¿Qué incluye el reporte PDF?**
✔ **Tabla con métricas clave**  
✔ **Gráfico de barras**: Comparación de ganancias brutas y beneficios  
✔ **Gráfico de dispersión**: Relación entre ganancias brutas y beneficios  
✔ **Gráfico de pastel**: Margen de ganancia medio por país  
✔ **Gráfico de barras**: Beneficios totales por país  

El archivo final se guarda como `output/reporte_final.pdf`.

---

## **🛠 Tecnologías y Librerías**
- **`pandas`** → Procesamiento y análisis de datos  
- **`matplotlib`** → Creación de gráficos y visualización de datos  
- **`reportlab`** → Generación del informe en PDF  

---

## **💡 Mejoras Futuras**
- 📝 Permitir que el usuario seleccione el CSV de entrada.  
- 📊 Agregar más gráficos personalizados.  
- 🌎 Internacionalización con diferentes idiomas.  

---

## **📄 Licencia**
Este proyecto se distribuye bajo la licencia **MIT**, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente.  

📌 **Contribuciones y mejoras son bienvenidas**. ¡Siéntete libre de hacer un fork y mejorar el proyecto! 🚀  

---

### 🎯 **Listo para subirlo a GitHub**
1. Asegúrate de que el **repositorio está creado** en GitHub.  
2. **Agrega y sube los archivos** con:
```bash
git init
git add .
git commit -m "Versión inicial del generador de reportes"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```
3. 🎉 ¡Listo! Ya tienes tu proyecto en GitHub con una documentación clara.  

Si necesitas personalizar más el `README.md`, dime y te ayudo a adaptarlo. 🚀😃
