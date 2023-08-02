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

# Load the Excel file
data = pd.read_csv('database.csv')

#sidebar menu & filters
st.sidebar.image("BaseFirmaLogo.png", caption="Your Go-To Transfer Pricing Firm in the Americas")
st.sidebar.header("Aplicar los filtros")
filtro_clientes = st.sidebar.multiselect(
    "Selecciona al Grupo Corporativo",
    options = data['Cliente'].unique(),
    default = data['Cliente'].unique(),
)

filtro_consultor = st.sidebar.multiselect(
    "Selecciona al Consultor",
    options = data['Consultor'].unique(),
    default = data['Consultor'].unique(),
)

filtro_consultor_sr = st.sidebar.multiselect(
    "Selecciona al Senior",
    options = data['Senior'].unique(),
    default = data['Senior'].unique(),
)

filtro_gerente = st.sidebar.multiselect(
    "Selecciona al Gerente 1️⃣",
    options = data['Gerente'].unique(),
    default = data['Gerente'].unique(),
)



# st.image("BaseFirmaLogo.png", width=150)
st.header('KPIs Dashboard')

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
        consultor = st.selectbox("Seleciona al Consultor:", consultores)
        senior = st.selectbox("Seleciona al Consultor Sr:", consultores_sr)
        gerente = st.selectbox("Seleciona al Gerente:", gerentes)

    with col3:
        tiempo_est = st.number_input("Horas Estimadas")
        tiempo_real = st.number_input("Horas Reales")
        fecha_est = st.date_input("Fecha Estimada de Entrega", datetime.date(2023,1,1))
        fecha_real = st.date_input("Fecha Real de Entrega", datetime.date(2023,1,1))

    submit_button = st.form_submit_button(label='Add Record')

# If the form is submitted, add the new record to the DataFrame
if submit_button:
    new_record = {"Cliente": cliente, "Sociedad": sociedad, "Proyecto": proyecto, "Consultor": consultor, "Senior": senior, "Gerente": gerente, "Tiempo estimado de Actividad": tiempo_est, "Fecha Planeada": fecha_est,
                 "Fecha de entrega efectiva": fecha_real, "Tiempo Real": tiempo_real}
    new_row = pd.DataFrame([new_record])
    data = pd.concat([data, new_row], ignore_index=True)
    # Save the updated DataFrame to the CSV file
    data.to_csv('database.csv', index=False)

# Display the updated data in a dataframe
st.write("Updated Data:")

kpis_empleado = data.query(
    "Cliente==@grupos & Consultor==@consultores & Senior==@consultores_sr & Gerente==@gerentes"

tab1, tab2, tab3 = st.tabs(["KPIs por Empleado", "KPIs Por Proyecto", "Data"])

with tab1:
    st.subheader("KPI's por empleado")
    st.dataframe("kpis_empleado")
with tab2:
    st.subheader("KPI's por Proyecto")
with tab3:
    # Display the data in a dataframe
    with st.expander("Tabla"):
        st.dataframe(data)







st.dataframe(data)
