import streamlit as st 
from PIL import Image

def about():
    
    st.title("Sobre Nosostros")
    
    st.write("¡Bienvenidos a nuestro equipo!")
    
    st.write("Somos un grupo de alumnos apasionados del Data Dcience, con el proyecto realizado hemos puesto en práctica nuestros conocimientos para transformar datos en conocimientos valiosos.")

    st.markdown("""Pertenecemos al BootCamp Data Science de : 
                       [Hack a Boss](https://www.hackaboss.com/).""")
    

    col1, col2, col3, col4 = st.columns(4)
     
    with col1:

        # Abrir la imagen local
        image = Image.open("sources/Manuel_linkedin.jpg")

        # Mostrar la imagen en Streamlit
        st.image(image, caption="Manuel Romero Briones", use_column_width=True)

        # Agregar un enlace
        st.write("[LinkedIn Profile](http://www.linkedin.com/in/manuelromerobriones)")

    
    with col2:

        # Abrir la imagen local
        image = Image.open("sources/rafa_linkedin.jpeg")

        # Mostrar la imagen en Streamlit
        st.image(image, caption="Rafael Quintero Moraga", use_column_width=True)

        # Agregar un enlace
        st.write("[LinkedIn Profile](http://www.linkedin.com/in/rafael-quintero-moraga-32a75910b)")


    with col3:

        # Abrir la imagen local
        image = Image.open("sources/teri_linkedin.png")

        # Mostrar la imagen en Streamlit
        st.image(image, caption="Tere Ruiz Fernández", use_column_width=True)

        # Agregar un enlace
        st.write("[LinkedIn Profile](http://www.linkedin.com/in/tere-ruiz-fernández)")

    with col4:

        # Abrir la imagen local
        image = Image.open("sources/ale_linkedin.jpeg")

        # Mostrar la imagen en Streamlit
        st.image(image, caption="Alejandro Fernández Perez", use_column_width=True)

        # Agregar un enlace
        st.write("[LinkedIn Profile](http://www.linkedin.com/in/alejandro-fp82)")

    st.info("Y como no podía ser de otra manera, aquí las pruebas de nuestro cliente satisfecho.")
    image = Image.open("sources/Dani_ozimandias.jpg")
        
    st.image(image            = image,
         caption          = "Gracias Profe",
         use_column_width = True )   
    pass

if __name__=="__about__":
    about()