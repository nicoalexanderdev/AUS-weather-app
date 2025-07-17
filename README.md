# 🌤️ AUS-Streamlit – Explorador del Clima en Australia

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit** que permite explorar datos climáticos históricos de diferentes regiones de Australia. Está orientado tanto a fines educativos como exploratorios en el contexto del análisis de datos.

## 🔍 Descripción

La aplicación permite visualizar y analizar variables meteorológicas como:

- Temperatura máxima y mínima
- Precipitaciones
- Evaporación
- Velocidad del viento
- Humedad relativa

Se utilizan filtros dinámicos por **ciudad**, **año**, y **mes**, así como visualizaciones gráficas interactivas para facilitar la interpretación de los datos.

## 📊 Dataset

El conjunto de datos proviene de registros meteorológicos históricos proporcionados por [Bureau of Meteorology Australia](http://www.bom.gov.au/) y contiene información desde el año 2008 hasta 2017.

### Estructura de columnas (ejemplos):

- `Date`: Fecha de la observación
- `Location`: Ciudad australiana
- `MinTemp`, `MaxTemp`: Temperaturas mínima y máxima
- `Rainfall`: Nivel de precipitaciones (mm)
- `WindSpeed9am`, `WindSpeed3pm`: Velocidad del viento
- `Humidity9am`, `Humidity3pm`: Humedad relativa
- `RainToday`, `RainTomorrow`: Variables categóricas para predicción de lluvia

## 🚀 Cómo ejecutar la app

1. Clona este repositorio:

```bash
git clone https://github.com/nicoalexanderdev/AUS-Streamlit.git
cd AUS-Streamlit
