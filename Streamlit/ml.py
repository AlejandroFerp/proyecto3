import streamlit as st
import numpy as np
from PIL import Image
import pickle
from modules.funciones_ml import read_data_modelo, load_model, read_data

import sklearn 
import pyarrow.parquet as pq
import pandas as pd
import plotly.express as px
import joblib
import dill


def ml():
    st.subheader(body = "Predicción del Precio :robot_face:")

    st.markdown(body = """En esta sección podrás ingresar las cararcterísticas de tu vehículo deseado y automáticamente predecimos su precio**_.""")

    st.sidebar.markdown("*"*10)
    
    # uploaded_file = st.sidebar.file_uploader(label = "Upload your input CSV file", type = ["csv"])
   
    # st.sidebar.markdown("*"*10)

    # data_input, = None

    # if uploaded_file is not None:
        
    #     data = pd.read_csv(filepath_or_buffer = uploaded_file)
        
    #     data_input = data.iloc[:,1:]

    # x_scaler, y_scaler, model = load_model()    

    # min_Cv, min_Año, min_Kms, = x_scaler.data_min_ 

    # max_Cv, max_Año, max_Kms, = x_scaler.data_max_  

    # min_Precio, max_Precio = y_scaler.data_min_, y_scaler.data_max_

    # Hay que leer el csv de los datos
    
    df = read_data()

    # with st.form("User's Input:"):
        
    coche_marca = st.selectbox(label = "Marca", options = df["Marca"].unique())

    df1 = df[df["Marca"] == coche_marca]

    coche_modelo = st.selectbox(label   = "Modelo",
                                options = df1["Modelo"].unique())
    
    df2 = df1[df1["Modelo"] == coche_modelo]

    coche_combustible = st.selectbox(label = "Combustible", options = df2["Combustible"].unique())

    coche_provincia = st.selectbox(label = "Provincia", options = df["Provincia"].unique())

    coche_cv = st.number_input(label = "Cv", ) # options = df["Cv"].unique()

    coche_año = st.number_input(label = "Año", ) # options = df["Año"].unique()

    coche_km =  st.number_input(label = "Kms", ) # options = df["Kms"].unique()

    submitted = st.button("Submit")

    if submitted:
        # Modelo con input de usuario

        # fila = [Marca, Modelo, Combustible, Provincia, Cv, Año, Kms,Precio]

        # datos = preprocesamiento_ml(fila)

        # yhat = ml_modelo.predict(datos)

        yhat, r2 = load_model(Marca = coche_marca, Modelo = coche_modelo, Combustible = coche_combustible,
                            Provincia = coche_provincia, Cv = coche_cv, Año = coche_año, Kms = coche_km)
        st.write("Predicción")
        st.write(yhat)

        st.write("r2")
        st.write(r2)










    
    #data input

    # loaded_model = joblib.load('C:\Users\terer\Desktop\Streamlit\Proyecto_nuevo\sources\modelo.parquet')
    
    # prediction = loaded_model.predict(seleccion)
    
    # # # with open("sources/modelo.parquet", "br") as file:
    # # #     ml_modelo = parquet.load(file) # Cambiar estoa parquet
        
    # # table = pq.read_table('/sources/modelo.parquet')
    # # ml_modelo = table.to_pandas()
        
    # with open ("sources/model.pkl", mode = "br") as file:
    #     model = pickle.load(file) 

    
    # with st.form("User's Input:"):
        
    #      coche_marca = st.select_box(label = "Marca", options = df["Marca"].unique())
        
    #      coche_modelo = st.select_box(label   = "Modelo",
    #                                   options = df[df["Marca"] == coche_marca]["Modelo"].unique())
        
    #      coche_combustible = st.select_box(label = "Combustible", options = df["Combustible"].unique())
        
    #      coche_provincia = st.select_box(label = "Provincia", options = df["Provincia"].unique())
        
    #      coche_cv = st.number_input(label = "Cv", options = df["Cv"].unique())
        
    #      coche_año = st.number_input(label = "Año", options = df["Año"].unique())
        
    #      coche_km =  st.number_input(label = "Kms", options = df["Kms"].unique())
        
        
        
    #      submitted = st.form_submit_button("Submit")
        
    #      if submitted:
    #          # Modelo con input de usuario
            
    #          fila = [Marca, Modelo, Combustible, Provincia, Cv, Año, Kms,Precio]
            
    #          datos = preprocesamiento_ml(fila)
            
    #          yhat = ml_modelo.predict(datos)
            
    #          st.write(yhat)
    
    
    # Provincia = st.selectbox("Selecciona una provincia:", df['Provincia'].unique())
    # Marca = st.selectbox("Selecciona una marca:", df['Marca'].unique())
    # Modelo = st.selectbox("Selecciona un modelo:", df[df['Marca'] == Marca]['Modelo'].unique())
    # Combustible = st.selectbox("Selecciona una combustible:", df['Combustible'].unique())
    # Ano = st.number_input("Ingresa el año del vehículo:", min_value=1978, max_value=2023)
    # Cv = st.number_input("Ingresa el cv:", min_value=1, max_value=999)

    # if st.button("Guardar Selección"):
    #     seleccion = [Provincia, Marca, Modelo, Combustible, Ano, Cv]
        
    #     prediction = loaded_model.predict(seleccion)
        
    #     st.write(seleccion)
        
    # prediction = loaded_model.predict(seleccion)
    # print("Predicción:", prediction)

    # Provincia = st.selectbox("Selecciona una provincia:", df['provincia'].unique())
    # Marca = st.selectbox("Selecciona una marca:", df['Marca'].unique())
    # Modelo = st.selectbox("Selecciona un modelo:", df[df['Marca'] == Marca]['Modelo'].unique())
    # Combustible = st.selectbox("Selecciona una combustible:", df['Combustible'].unique())
    # Ano = st.number_input("Ingresa el año del vehículo:", min_value=1978, max_value=2023)
    # Cv = st.number_input("Ingresa el cv:", min_value=1, max_value=999)
    # Kms = st.number_input("Ingresa los kilometros:", min_value=1, max_value=999999)
    # if st.button("Guardar Selección"):
    #     seleccion = [Marca,Modelo,Combustible,Provincia]
    #     st.write(seleccion)
    # with open('encoder.pkl', 'rb') as file:
    #     loaded_function = dill.load(encoder.pkl) 
    #     array_codificado = loaded_function(seleccion)       
    #     print(array_codificado)
    
    # pass


if __name__=="__ml__":
    ml()