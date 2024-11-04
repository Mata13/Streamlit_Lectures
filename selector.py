# Importamos las librerias que vamos a usar
import streamlit as st
import pandas as pd
import PIL as Image

#### Trabajamos con selectores ####

# Creamos la funcion principal que va a llevar todo lo que tiene que ver con streamlit
def main():
  st.title("Curso de Streamlit")
  # Selectbox
  opcion = st.selectbox(
		'Elige tu fruta favorita',
  ['Manzana', 'Naranja', 'Platano', 'Fresa']
	)
  st.write(f'Tu fruta favorita es: {opcion}')

  # Multiselect
  opciones = st.multiselect(
		'Selecciona tus colores favoritos',
  ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Negro', 'Blanco']
	)
  st.write('Tus colores favoritos son:', opciones)

  # Slider
  edad = st.slider(
		'Selecciona tu edad',
  min_value=0,
  max_value=100,
  value=25, # valor incial
  step=1
	)
  st.write('Tu edad es:', edad)

  # Select Slider
  nivel = st.select_slider('Selecciona tu nivel de satisfaccion', options=['Muy Bajo', 'Bajo', 'Medio', 'Alto', 'Muy Alto'], value='Medio')
  st.write('Tu nivel de satisfraccion es:', nivel)

  # Imagenes en Streamline
  st.image("https://picsum.photos/800") # esto muestra una img aleatoria

if __name__ == '__main__':
  main()