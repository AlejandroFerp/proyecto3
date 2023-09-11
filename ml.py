import streamlit as st
import numpy as np
from PIL import Image
import pickle
from Modules.fun import preprocesamiento_ml
import sklearn

def ml():
    
    st.subheader(body = "Machine Learning Model :robot_face:")

    st.markdown(body = """From the `Exploratory Data Analysis` section we conclude that there is a linear relationship
                          between _**Fuel Consumption City**_ and _**CO2 Emissions**_.""")
    st.markdown(body = """Use the sidebar to try our models. We have built a model for each type of `Fuel Type`.""")
    # Hay que leer el csv de los datos
    
    df = pd.read_csv("sources/stream.csv")
    
    with open("/sources/modelo.parquet", "br") as file:
        ml_modelo = parket.load(file) # Cambiar estoa parquet
        
        
    with st.form("User's Input:"):
        coche_marca = st.select_box(label = "Marca", options = df["Marca"].unique())
        coche_km =  st.number_input()
        coche_modelo = st.select_box(label   = "Modelo",
                                     options = df[df["Marca"] == coche_marca]["Modelo"].unique())
        coche_año = st.number_input()
        coche_cv = st.number_input()
        coche_provincia = st.select_box(label = "Provincia", options = df["Provincia"].unique())
        coche_combustible = st.select_box(label = "Combustible", options = df["Combustible"].unique())
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            # Modelo con input de usuario
            
            fila = [coche_marca, ...]
            
            datos = preprocesamiento_ml(fila)
            
            yhat = ml_modelo.predict(datos)
            
            st.write(yhat)
            
            
    
    

if __name__ == "__ml__":
    ml()