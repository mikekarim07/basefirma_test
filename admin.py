import streamlit as st
import pandas as pd
import datetime


st.set_page_config(
    page_title="Base Firma",
    page_icon="⏱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:miguel.karim@karimortega.com'
    }
)

st.image("BaseFirmaLogo.png", width=150)
st.header('KPIs Dashboard')

# Load the Excel file
data = pd.read_csv('database.csv')

# Display the data in a dataframe
with st.expander("Tabla"):
    st.dataframe(data)
#--settings--
gerentes = ["Jaime Romero", "Karen Ramos"]
consultores = ["Jorge Amaya", "Leslie Castillo", "Martin Rivera", "Rebeca Sandoval", "Otro"] 
consultores_sr = ["Brenda Salazar", "Christian Huitron", "Guillermo Pato"]
grupos = ["CHUBB", "ACCIONA", "Crehana", "Corona", "Adabe Capital", "Luxottica", "Grupo IAMSA", "Melia"]
sociedades = ["ABA Asistencias", "ABA Garantias SA de CV", "Acciona Agua Mexico S RL CV (AGUA)", "Acciona Energía México, S. de R.L. de C.V. (ENERGIA)", "Acciona Energía Servicios México, S. de R.L. de C.V. (ENERGIA)", "Acciona Eólica Santa Cruz S. R.L. de C.V. (ENERGIA)"
              "Acciona Forwarding (SERVICES)", "Acciona Infraestructuras México, S.A. de C.V. (INFRAESTRUCTURA)", "Acciona Infraestructuras Residenciales México, S.A. de C.V. (INFRAESTRUCTURA)"]


# Create a form to create a new record
with st.form("Create new record", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        cliente = st.selectbox("Seleciona al Grupo:", grupos)
        sociedad = st.selectbox("Seleciona la entidad legal:", sociedades)
        proyecto = st.text_input("Proyecto")
    
    with col2:
        consultor = st.selectbox("Seleciona al Grupo:", consultores)
        senior = st.selectbox("Seleciona al Grupo:", consultores_sr)
        gerente = st.selectbox("Seleciona al Grupo:", gerentes)

    with col3:
        tiempo_est = st.number_input("Horas Estimadas")
        tiempo_real = st.number_input("Horas Reales")
        fecha_est = st.date_input("Fecha Estimada de Entrega", datetime.date(2023,1,1))
        fecha_real = st.date_input("Fecha Real de Entrega", datetime.date(2023,1,1))

    submit_button = st.form_submit_button(label='Add Record')

# If the form is submitted, add the new record to the DataFrame
if submit_button:
    new_record = {"Cliente": cliente, "Sociedad": sociedad}
    new_row = pd.DataFrame([new_record])
    data = pd.concat([data, new_row], ignore_index=True)
    # Save the updated DataFrame to the CSV file
    data.to_csv('database.csv', index=False)

# Display the updated data in a dataframe
st.write("Updated Data:")
st.dataframe(data)
