import streamlit as st
from modules.funciones_ml import read_data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def page_app_func():
    
    #st.title(body = "Proyecto Streamlit")
    
    st.subheader(body = "Inicio :red_car:")

    st.write("Bienvenidos a la platarorma **Cars MART** realizado con **Streamlit**.")
        
    st.markdown("""Los datos para esta plataforma se obtuvieron de : 
                       [Auto Scout 24](https://www.autoscout24.es/).""")

        
    st.write("Explora el mundo del aprendizaje automático y la predicción de precios de coches de segunda mano en nuestra plataforma. ")


    st.write("""Nuestro modelo utiliza datos clave como marca, año, kilometraje, potencia, combustible incluso la provincia en el territorio español de mas de 250.000 vehículos, para así, ofrecerte una estimación precisa del valor del automóvil que te interesa.""")
     
    df = read_data()
    
    with st.expander(label = "Base de Datos", expanded = False):
        st.dataframe(df)   
        
    st.write("""**¿Cómo funciona?**""")
        
    st.write("""Puedes navegar a traves de nuestra web de una forma interactiva seleccionando tus intereses.""")

  

   

    #     # Widget para subir archivos
    # archivo = st.file_uploader("sources/Impala.gif", type=["gif"])

    # if archivo is not None:
    # # Mostrar el GIF
    #     st.image(archivo, caption='sources/Impala.gif', use_column_width=True)



    # col1, col2 = st.columns(2)


    # with col1:
    #     st.video ("sources/Impala", format='gif")


    # with col2:
    #     st.write("""Ésto no te pasará con nosotros""")
    
    # fig_scatter = px.scatter(data_frame = df,
    #                 x          = "Cv",
    #                 y          = "Precio",
    #                 color      = "Combustible",
    #                 opacity    = 0.5)
    
    
    # plt.figure(figsize=(15, 6))
    # sns.countplot(data=df, x='Año', palette='Set1')
    # plt.xlabel('Año')
    # plt.ylabel('Número de Coches')
    # plt.title('Distribución de Coches por Año')
    # plt.xticks(rotation=45)
    # plt.show()
    
    # st.title("Aqúi podrás comenzar a explorar:")
        
    # st.info("Para un análisis más profundo, haz clic en la pestaña, Analiza las características.")
    
    pass
if __name__=="__page_app_func__":
    page_app_func()
    