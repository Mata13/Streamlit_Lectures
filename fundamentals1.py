# Importamos las librerias que vamos a usar
import streamlit as st
import pandas as pd

##### Vamos a mostrar un dataframe #####

df = pd.read_csv('CR_Flux_7m.txt')

#Creamos la funcion principal que va a llevar todo lo que tiene que ver con streamlit
def main():
  st.title("Dataframe con los resultados de las simulaciones con CORSIKA")
  st.header("Simulacion a 7 m.s.n.m.")
  st.dataframe(df)

  # Podemos poner codigo dentro del proyecto
  codigo = """
  def saludar():
	print("Hola")
  """
  st.code(codigo, language="python")

if __name__ == '__main__':
  main()