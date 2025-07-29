# 🌤️ AUS-Streamlit – Explorador del Clima en Australia [🔗](https://aus-weather-app-cdsfnhx9nm6kefpttjdbaj.streamlit.app/)


<img width="958" height="456" alt="AUS-weather-app" src="https://github.com/user-attachments/assets/fed28ff3-1ab7-4d41-83ec-247d93f77286" />


Este proyecto es una aplicación web interactiva desarrollada con **Streamlit** que permite explorar datos climáticos históricos de diferentes regiones de Australia. Está orientado tanto a fines educativos como exploratorios en el contexto del análisis de datos. [Link de la App](https://aus-weather-app-cdsfnhx9nm6kefpttjdbaj.streamlit.app/)

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
git clone https://github.com/nicoalexanderdev/AUS-weather-app.git
cd AUS-weather-app
```

2. Crea y activa el entorno virtual con uv:

```bash
uv venv .venv
source .venv/bin/activate        # En Linux/macOS
.\.venv\Scripts\activate         # En Windows
```

3. Instala las dependencias definidas en pyproject.toml

```bash
uv pip install -r uv.lock
```

3. Ejecuta la app:

```bash
uv run streamlit run streamlit_app/main.py
```
**✅ Asegúrate de tener Python 3.8+ y uv instalado. Puedes instalar uv con:**
```bash
pip install uv
```


## 🛠️ Tecnologías utilizadas

- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn


## 🙌 Autor

- Desarrollado por Nicolás Oses Pérez – [LinkedIn](https://www.linkedin.com/in/nicolas-oses/)
- Estudiante de Ingeniería en Informática | Mención Ciencia de Datos
- DuocUC – 2025
