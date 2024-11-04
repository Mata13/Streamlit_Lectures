# Importamos las librerias que vamos a usar
import streamlit as st
import pandas as pd
import PIL as Image

### Trabajamos con Inputs ###

# Creamos la funcion principal que va a llevar todo lo que tiene que ver con streamlit
def main():
  st.title("Curso de Streamlit")
  # Input
  nombre = st.text_input("Ingresa tu nombre")
  st.write(nombre)

  # Text area
  mensaje = st.text_area("Ingresa tu mensaje", height=100)
  st.write(mensaje)

  # Entrada de numeros
  numero = st.number_input('Ingresa un numero', 1, 25, step=1)
  st.write(numero)

  # Entrada de fechas
  cita = st.date_input("Selecciona una fecha para la cita")
  st.write('La cita esta programada para la siguiente fecha:', cita)

  # Entrada de hora (tiempo)
  hora = st.time_input("Selecciona la hora de la cita")
  st.write('La cita queda programada  a las:', hora)

  # Seleccion de color
  color = st.color_picker("Selecciona un color")
  st.write(color)

if __name__ == '__main__':
  main()