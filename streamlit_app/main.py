import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import os

st.set_page_config(layout="wide") 

st.title("App del clima en Australia")

df = pd.read_csv("data/weatherAUS.csv")
geo = pd.read_csv("data/geo_australia.csv", sep=";")
df_geo = df.merge(geo, on='Location', how='left')

component1, component2, component3 = st.columns(3)

with component1:
    st.image(os.path.join(os.getcwd(), "static", "sydney.jpg"), width=500)
    st.divider()
    st.header("Dataset original")
    

    st.subheader("Metricas")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Rows", value=df.shape[0])
        st.metric(label="Total Localidades", value=df['Location'].nunique())

    with col2:
        st.metric(label="Total Columns", value=df.shape[1])
        st.metric(label="Total Datos Nulos", value=df.isna().sum().sum())
        


    st.dataframe(df)

with component2:
    st.header("Charts")

    datos_temp = df_geo.groupby(['Location', 'Latitude', 'Longitude'])['MaxTemp'].mean().reset_index()

    fig_1 = px.scatter_geo(
    datos_temp,
    lat='Latitude',
    lon='Longitude',
    text='Location',
    color='MaxTemp',
    color_continuous_scale='Inferno',
    size='MaxTemp',
    projection='natural earth',
    title='Promedio General de Temperatura Máxima por Ciudad en Australia',
    hover_name='Location',
    hover_data={'MaxTemp': ':.2f', 'Latitude': True, 'Longitude': True}
)

    # Mejorar estilo del mapa
    fig_1.update_traces(marker=dict(line=dict(width=1, color='black')))
    fig_1.update_geos(
        lataxis_range=[-45, -10],
        lonaxis_range=[110, 155],
        visible=True,
        showcountries=True,
        showsubunits=True
    )
    fig_1.update_layout(coloraxis_colorbar=dict(title='MaxTemp Prom.'))

    # Mostrar en Streamlit
    st.plotly_chart(fig_1, use_container_width=True)

    st.divider()

    datos_rain = df_geo.groupby(['Location', 'Latitude', 'Longitude'])['Rainfall'].mean().reset_index()

    # Crear el mapa
    fig_2 = px.scatter_geo(
        datos_rain,
        lat='Latitude',
        lon='Longitude',
        text='Location',
        color='Rainfall',
        color_continuous_scale='Blues',
        size='Rainfall',
        projection='natural earth',
        title='Promedio General de Lluvia por Ciudad en Australia',
        hover_name='Location',
        hover_data={'Rainfall': ':.2f', 'Latitude': False, 'Longitude': False}
    )

    # Mejorar estilo del mapa
    fig_2.update_traces(marker=dict(line=dict(width=1, color='black')))
    fig_2.update_geos(
        lataxis_range=[-45, -10],
        lonaxis_range=[110, 155],
        visible=True,
        showcountries=True,
        showsubunits=True
    )
    fig_2.update_layout(coloraxis_colorbar=dict(title='Lluvia Prom. (mm)'))

    # Mostrar en Streamlit
    st.plotly_chart(fig_2, use_container_width=True)

with component3:
    # Título de la app
    st.header("🌤️ Predicción de Temperatura Máxima")

    # Ruta del modelo
    model_path_reg = os.path.join("models_ML/models", "ridge_regression.pkl")
    model_path_cla = os.path.join("models_ML/models", "gradient_boosting_classifier.pkl")

    # Ruta Scalers
    scaler_path = os.path.join("models_ML/scalers", "scaler_reg.pkl")
    scaler_y_path = os.path.join("models_ML/scalers", "scaler_target.pkl")
    scaler_cla_path = os.path.join("models_ML/scalers", "scaler_cla.pkl")

    # Ruta LabelEncoders
    le_estacion_path = os.path.join("models_ML/encoders", "le_estacion.pkl")
    le_location_path = os.path.join("models_ML/encoders", "le_location.pkl")

    # Cargar modelo
    @st.cache_resource
    def load_model():
        return joblib.load(model_path_reg)
    
    @st.cache_resource
    def load_model_cla():
        return joblib.load(model_path_cla)
    
    @st.cache_resource
    def load_scaler():
        return joblib.load(scaler_path)
    
    @st.cache_resource
    def load_scaler_y():
        return joblib.load(scaler_y_path)
    
    @st.cache_resource
    def load_scaler_cla():
        return joblib.load(scaler_cla_path)
    
    @st.cache_resource
    def load_estacion_le():
        return joblib.load(le_estacion_path)
    
    @st.cache_resource
    def load_location_le():
        return joblib.load(le_location_path)

    model_ridge = load_model()
    model_gradient_boost = load_model_cla()
    scaler = load_scaler()
    scaler_y = load_scaler_y()
    scaler_cla = load_scaler_cla()
    le_estacion = load_estacion_le()
    le_location = load_location_le()

    # Obtener los valores originales (ordenados)
    estaciones = le_estacion.classes_
    locations = le_location.classes_

    # Formulario de entrada
    with st.form("prediction_form"):
        st.subheader("📋 Ingrese los datos climáticos:")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            min_temp = st.slider("MinTemp (°C)", value=15.0, step=0.5, min_value=-9.0, max_value=32.0)
            pressure_3pm = st.slider("Pressure3pm (hPa)", value=1000.0, step=0.1, min_value=986., max_value=1040.)
        
        with col2:
            temp_3pm = st.slider("Temp3pm (°C)", value=22.0, step=0.5, min_value=-5.0, max_value=46.0)
            #estacion_le = st.number_input("Estacion_le (codificado)", min_value=0., max_value=3.0, step=1.0)
            estacion = st.selectbox('Estacion', estaciones)

        with col3:
            humidity_3pm = st.slider("Humidity3pm (%)", value=50.0, step=1., min_value=0., max_value=100.)
            #location_le = st.number_input("Location_le (codificado)", min_value=0, max_value=48, step=1)
            location = st.selectbox('Location', locations)

        submitted_reg = st.form_submit_button("Predecir temperatura máxima")
    # Si se envió el formulario
    if submitted_reg:
        # Codificar estación y localidad
        estacion_le = le_estacion.transform([estacion])[0]
        location_le = le_location.transform([location])[0]
        input_data = pd.DataFrame([[min_temp, temp_3pm, humidity_3pm, pressure_3pm, estacion_le, location_le]],
                                  columns=["MinTemp", "Temp3pm", "Humidity3pm", "Pressure3pm", "Estacion_le", "Location_le"])

        # Transformar usando el scaler cargado (ya entrenado)
        input_scaled_array = scaler.transform(input_data)
        input_scaled = pd.DataFrame(input_scaled_array, columns=input_data.columns)

        # Predicción y desnormalización
        prediction = model_ridge.predict(input_scaled).reshape(-1, 1)
        prediction_original = scaler_y.inverse_transform(prediction)

        st.success(f"🌡️ Temperatura máxima estimada: **{prediction_original[0][0]:.2f}°C**")


    st.divider()

    # Título de la app
    st.header("⛈️ Predicción de Lluvia")

    # Formulario de entrada
    with st.form("rain_form"):
        st.subheader("📋 Ingrese los datos climáticos para lluvia:")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            humidity_3pm_rain = st.slider("Humidity3pm (%)", value=50.0, step=1., min_value=0., max_value=100.)
            cloud_3pm = st.slider("Cloud3pm (octal)", value=3., step=1., min_value=0., max_value=8.)

        with col2:
            cloud_9am = st.slider("Cloud9am (octal)", value=3., step=1., min_value=0., max_value=8.)
            estacion_rain = st.selectbox('Estación', estaciones, key="estacion_rain")

        with col3:
            rain_today = st.slider("¿Llovió hoy? (0: No, 1: Sí)", value=0., step=1., min_value=0., max_value=1.)
            location_rain = st.selectbox('Localidad', locations, key="location_rain")

        submitted_rain = st.form_submit_button("Predecir lluvia")

    if submitted_rain:
        estacion_le_rain = le_estacion.transform([estacion_rain])[0]
        location_le_rain = le_location.transform([location_rain])[0]

        input_data = pd.DataFrame([[humidity_3pm_rain, cloud_3pm, cloud_9am, rain_today, location_le_rain, estacion_le_rain]],
                                columns=["Humidity3pm", "Cloud3pm", "Cloud9am", "RainToday", "Location_le", "Estacion_le"])

        input_scaled = pd.DataFrame(scaler_cla.transform(input_data), columns=input_data.columns)

        prediction = model_gradient_boost.predict(input_scaled)
        prob = model_gradient_boost.predict_proba(input_scaled)[0][1]

        rain_label = "🌧️ Sí, probablemente lloverá." if prediction[0] == 1 else "🌤️ No, no se espera lluvia."

        st.success(f"⛈️ Predicción de lluvia: **{rain_label}**")
        st.metric("Confianza", f"{prob:.2%}")


if __name__ == "__main__":
    pass
