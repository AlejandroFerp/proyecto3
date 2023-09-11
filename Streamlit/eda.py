import streamlit as st 
import pandas as pd
from modules.funciones_ml import read_data
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


def eda():
    
    st.subheader(body = "Base de Datos Interactiva :bar_chart:")
    st.write("Aquí puedes realizar desde una consulta de información específica hasta generar una serie de visualizaciones dinámicas que te facilitarán la comprensión y el análisis de los datos.")
    df = read_data()
    
    
    # Convertir la columna 'Cv' a tipo numérico
    df['Cv'] = pd.to_numeric(df['Cv'], errors='coerce')
    
    # Convertir la columna 'Precio' a tipo numérico (float)
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce').astype(float)

    # Obtener la lista única de años
    unique_years = sorted(df['Año'].unique())

    # Obtener la lista única de caballos de fuerza (Cv)
    unique_Cv = sorted(df['Cv'].unique())

    # Obtener la lista única de marcas
    unique_marca= sorted(df['Marca'].unique())

    # Obtener la lista única de combustibles
    unique_combustible=  sorted(df['Combustible'].unique())
    
    # Obtener la lista única de provincias
    unique_provinces = sorted(df['Provincia'].unique())

    # Obtener los valores mínimos y máximos de precios
    min_price = df['Precio'].min()
    max_price = df['Precio'].max()

    # Obtener las listas únicas para los widgets de selección múltiple y sliders
    

    # En la primera fila, crear tres columnas
    col1, col2, col3 = st.columns(3)

    # Columna 1
    with col1:
        # Agregar un widget de selección múltiple para elegir marcas de automóviles
        selected_marca= st.multiselect("Seleccione una o varias marcas de automóviles:", unique_marca, default=unique_marca[:10])
    # Columna 2
    with col2:
        # Agregar un widget de selección múltiple para elegir combustibles de automóviles
        selected_combustibles= st.multiselect("Seleccione una o varias combustibles de automóviles:", unique_combustible, default=unique_combustible[:10])

    # Columna 3
    with col3:
        # Agregar un widget de selección múltiple para elegir provincias
        selected_provinces = st.multiselect("Seleccione una o varias provincias:", unique_provinces, default=unique_provinces[:10])

    # En la segunda fila, crear tres columnas
    col4, col5, col6 = st.columns(3)

    # Columna 4
    with col4:
        # Agregar un filtro por año con un widget de rango (slider)
        min_year, max_year = st.slider("Filtrar por año:", min_value=min(unique_years), max_value=max(unique_years), value=(min(unique_years), max(unique_years)))

    # Columna 5
    with col5:
        # Agregar un filtro por caballos de fuerza (Cv) con un widget de rango (slider)
        min_Cv, max_Cv = st.slider("Filtrar por caballos de fuerza (Cv):", min_value=min(unique_Cv), max_value=max(unique_Cv), value=(min(unique_Cv), max(unique_Cv)))

    # Columna 6
    with col6:
        # Agregar un filtro por precio con un widget de rango (slider)
        min_price, max_price = st.slider("Filtrar por precio:", min_value=min_price, max_value=max_price, value=(min_price, max_price))

    # Configurar la lógica de filtro para marcas, provincias, año, caballos de fuerza (Cv) y precio
    if "Todas" in selected_marca:
        filtered_data = df[(df['Año'] >= min_year) & (df['Año'] <= max_year) & (df['Cv'] >= min_Cv) & (df['Cv'] <= max_Cv) & (df['Precio'] >= min_price) & (df['Precio'] <= max_price)]
    else:
        filtered_data = df[(df['Marca'].isin(selected_marca)) & (df['Año'] >= min_year) & (df['Año'] <= max_year) & (df['Cv'] >= min_Cv) & (df['Cv'] <= max_Cv) & (df['Precio'] >= min_price) & (df['Precio'] <= max_price)]

    if "Todas" not in selected_provinces:
        filtered_data = filtered_data[filtered_data['Provincia'].isin(selected_provinces)]
    
    st.write("En la siguiente tabla se muestra el resultado de los filtros.")
    
    df=filtered_data 
    st.write(df)
    
    
    # Scatter Plot
    # Calcular la media de "Cv" por marca y año
    st.subheader("Media de precio por Kilómetro del automóvil según combustible")
    media_por_kilometro_y_combusticle = df.groupby(['Combustible', 'Kms'])['Precio'].mean().reset_index()

    # Renombrar la columna 'Cv' a 'Media'
    media_por_Combustible_y_Precio = media_por_kilometro_y_combusticle .rename(columns={'Precio': 'MediaPrecio'})

    # Crear un nuevo DataFrame con las columnas 'Año', 'Media' y 'Marca'
    df_sidebar = media_por_Combustible_y_Precio [['Kms', 'MediaPrecio', 'Combustible']]
    df_sidebar = df_sidebar.sort_values(by='MediaPrecio', ascending=True)

    fig_scatter = px.scatter(data_frame = df_sidebar,
                        x          = "MediaPrecio",
                        y          = "Kms",
                        color      = "Combustible",
                        #size       = "360",
                        #title      = f"{make} Cars - Year: {model_year}",
                        opacity    = 0.5)
    
    st.plotly_chart(fig_scatter)
    fig_scatter1 = px.scatter(data_frame = df,
                        x          = "Precio",
                        y          = "Kms",
                        color      = "Combustible",
                        # size       = "Engine Size",
                        #title      = f"{make} Cars - Year: {model_year}",
                        opacity    = 0.5)
    
    st.plotly_chart(fig_scatter1)

    
    # Agrupar por 'Marca' y contar los valores
    Contar_por_marca = df['Marca'].value_counts().reset_index()
    Contar_por_marca.columns = ['Marca', 'Count']

    # Crear pie chart
    fig_pie = px.pie(
        data_frame=Contar_por_marca,
        names="Marca",
        values="Count",
        title="Distribucion por Marca"
    )
    st.plotly_chart(fig_pie)
        # Agrupar por 'Marca' y contar los valores
    Contar_por_marca = df['Combustible'].value_counts().reset_index()
    Contar_por_marca.columns = ['Combustible', 'Count']
    
    # Crear un pie chart
    fig_pie1 = px.pie(
        data_frame=Contar_por_marca,
        names="Combustible",
        values="Count",
        title="Distribucion por Combustible y Año"
    )

    # mostrar la grafica
    st.plotly_chart(fig_pie1)

    # Group by 'Combustible' and 'Año', and count the occurrences
    df_group = df.groupby(['Combustible', 'Año']).size().reset_index(name='Count')

    # Create the bar chart
    fig_bar = px.bar(
        data_frame=df_group,
        x="Año",
        y="Count",
        color="Combustible",
        text="Count",  # Show count values on top of bars
        title="Distribution of Combustible by Year"
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_bar)


    # Calcular la media de "Cv" por marca y año
    media_por_marca_y_año = df.groupby(['Marca', 'Año'])['Cv'].mean().reset_index()

    # Renombrar la columna 'Cv' a 'Media'
    media_por_marca_y_año = media_por_marca_y_año.rename(columns={'Cv': 'MediaCv'})

    # Crear un nuevo DataFrame con las columnas 'Año', 'Media' y 'Marca'
    nuevo_df = media_por_marca_y_año[['Año', 'MediaCv', 'Marca']]
    nuevo_df = nuevo_df.sort_values(by='Año', ascending=True)

    
    nuevo_df = pd.DataFrame(nuevo_df)

    # Ordenar el DataFrame por la columna 'Año' en orden ascendente
    nuevo_df = nuevo_df.sort_values(by='Año', ascending=True)

    # Crear un gráfico de línea utilizando Plotly Express
    line = px.line(data_frame=nuevo_df, x='Año', y='MediaCv', color='Marca')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(line)
    # Utiliza Plotly Express para crear el gráfico de caja 
    fig_box= px.box(data_frame=filtered_data, x="Marca", y="Precio", title="Distribución de Precios por Marca")

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_box)

    
    pass

if __name__=="__eda__":
    eda()