import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="📘")

st.title("📘 Resolviendo ecuaciones de primer grado")
st.write("Resuelve la siguiente ecuación para **x**:")

# Generar ecuación aleatoria: ax + b = c
a = random.randint(1, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)

# Calcular la solución
sol = (c - b) / a

# Mostrar ecuación
st.latex(f"{a}x + {b} = {c}")

# Input solo enteros
respuesta = st.number_input("Tu respuesta para x (solo enteros)", step=1)

# Botón para verificar
if st.button("Verificar"):
    if respuesta == sol and sol.is_integer():
        st.success("¡Correcto! 🎉")
        st.balloons()
    else:
        st.error("❌ Incorrecto, intenta de nuevo.")
        st.info(f"Pista: la respuesta correcta era {sol}")
