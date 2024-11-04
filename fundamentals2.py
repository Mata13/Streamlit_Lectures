# Importamos las librerias que vamos a usar
import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd

# Cambiamos es titulo de la pagina principal y algunos atributos
st.set_page_config(page_title='Fundamentals of Streamlit', page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

# Definimos la funcion principal que va a llevar todo lo que tiene que ver con streamlit
def main():
  st.title("Bienvenidos a SpaceMarc")
  st.sidebar.header("Navegacion") # barra lateral
  # Vamos a graficar algunas cosas del dataframe
  df = pd.read_csv("CR_Flux_7m.txt")
  st.dataframe(df) # se muestra el dataframe
  fig = px.line(df, x="Energy (GeV)", y="Photons", log_x=True, log_y=True, title="Distribucion de la energia de las particulas usando plotly")
  st.plotly_chart(fig)

if __name__ == '__main__':
  main()