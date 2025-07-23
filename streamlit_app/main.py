import streamlit as st
import pandas as pd
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
    st.header("Predictions")


if __name__ == "__main__":
    pass
