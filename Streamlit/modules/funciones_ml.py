from pyexpat import model
from tabnanny import filename_only
import numpy as np
import pandas as pd
import pickle
import base64
import sklearn as sk
import streamlit as st



PAGE_CONFIG = {"page_title"             : "Precio Cohces Segunda Mano",
                "page_icon"             : ":car:",
                "layout"                : "wide",
                "initial_sidebar_state" : "expanded"}

def read_data():
    
    df = pd.read_csv(filepath_or_buffer = "sources/stream.csv")
    
    return df
 
def read_data_modelo():
    
    df = pd.read_csv(filepath_or_buffer = "sources/final.csv")
    
    return df
 
 
    
def load_model(Marca, Modelo, Combustible, Provincia, Cv, Año, Kms):
    
   # Label Encoder (Marca, modelo, Combustible, Provincia)
   with open (file = f"sources/encoder.pkl", mode = "br") as file:
      label_encoders = pickle.load(file)

   # Modelo
   with open (file = f"sources/model.pkl", mode = "br") as file:
      model = pickle.load(file)

   # Scaler (X)
   with open (file = f"sources/x_scaler.pkl", mode = "br") as file:
      x_scaler = pickle.load(file)

   # Scaler (y)
   with open (file = f"sources/y_scaler.pkl", mode = "br") as file:
      y_scaler = pickle.load(file)
      
   with open (file = f"sources/r2.pkl", mode = "br") as file:
      r2 = pickle.load(file)

   # Preprocesamiento
   fila = np.array([[Marca, Modelo, Combustible, Provincia, Cv, Año, Kms]])

   st.write(fila)

   for num, encoder in enumerate(label_encoders):
      fila[:, num] = encoder.transform(fila[:, num])

   fila = x_scaler.transform(fila)

   yhat = model.predict(fila)

   yhat = y_scaler.inverse_transform(yhat.reshape(-1, 1))
    
   return yhat, r2

# def preprocesamiento():
    
   
    
#    return yhat