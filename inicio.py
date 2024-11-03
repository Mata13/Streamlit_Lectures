# Importamos las librerias que vamos a usar
import streamlit as st

# Creamos una funcion principal que va a llevar todo lo que tiene que ver con streamlit
def main():
  st.title("Curso de Streamlit") # seria como el h1 en html
  st.header("Esto es un encabezado") # seria un h2
  st.subheader("Esto seria un subencabezado") # seria un h3
  st.text("Hola, esto es un texto")

  # Podemos combinar texto con variables
  nombre = "SpaceMarc"
  st.text(f"Hola {nombre}, esto es un texto")
  st. markdown("## Esto es un markdown") # seria un h2

  # Podemos mostrar diferentes textos
  st.success("Exito!!!") # mensaje formateado
  st.warning("Esto es una advertencia")
  st.info("Esto es informacion")
  st.error("Esto es un error")
  st.exception("Esto es una excepcion")

  # Podemos mostrar texto
  st.write("Texto normal")
  st.write("## Esto es un texto de markdown")
  st.write(1 + 1) # solo se muestra el resultado de la operacion
  st.write(1 / 2) # solo se muestra el resultado

if __name__ == '__main__':
  main()

# Para correr el programa en la terminal ponemos ""streamlit run name.py"