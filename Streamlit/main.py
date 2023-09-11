import streamlit as st
from page_app import page_app_func
from ml import ml
from eda import eda
from about import about
from modules.funciones_ml import PAGE_CONFIG
from PIL import Image

st.set_page_config(** PAGE_CONFIG)


def main():
    
    
    menu = ["Inicio", "Base de Datos Interactiva", "Predicciones", "Sobre Nosotros" ] 
    
    page = st.sidebar.selectbox(label = "Menu", options = menu, index = 0)
    
    if page == "Inicio":
        
        page_app_func()
        
        pass
    
    elif page == "Base de Datos Interactiva":
        
        eda()
        pass
    
    elif page == "Predicciones":
        
        ml()
        pass
    
    else:
        
        about()
        
        pass
    
    
if __name__== "__main__":
    main()
    