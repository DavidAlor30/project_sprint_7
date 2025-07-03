import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis de anuncios de autos usados")

# Leer los datos
car_data = pd.read_csv(r'C:\Users\david\OneDrive\Escritorio\PROYECTO 7\vehicles_us.csv')

# Casillas de verificación
show_hist = st.checkbox('Mostrar histograma de odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión: precio vs odómetro')

# Mostrar histograma
if show_hist:
    st.write('Creación de un histograma del odómetro de los autos listados')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Mostrar gráfico de dispersión
if show_scatter:
    st.write('Gráfico de dispersión: Precio vs Odómetro')
    fig2 = px.scatter(car_data, x="odometer", y="price", opacity=0.2,
                      title="Relación entre odómetro y precio")
    st.plotly_chart(fig2, use_container_width=True)
