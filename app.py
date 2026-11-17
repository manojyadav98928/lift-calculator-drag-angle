import streamlit as st

st.title("Aircraft Lift Calculator")
st.write("Calculate lift force using aerodynamic equations.")

rho = st.number_input("Air density (kg/m³)", value=1.225)
velocity = st.number_input("Velocity (m/s)", value=50.0)
area = st.number_input("Wing area (m²)", value=10.0)
cl = st.number_input("Lift coefficient", value=0.5)

if st.button("Calculate Lift"):
    lift = 0.5 * rho * velocity**2 * area * cl
    st.success(f"Lift Force = {lift:.2f} N")
