import streamlit as st
import pandas as pd
import datetime

# Set Streamlit page configuration
st.set_page_config(
    page_title="Base Firma",
    page_icon="⏱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'Get Help': 'mailto:miguel.karim@karimortega.com'}
)
st.sidebar.image("BaseFirmaLogo.png", caption="Your Go-To Transfer Pricing Firm in the Americas")
st.sidebar.header('KPIs Dashboard')
st.sidebar.caption('Archivo de Excel con el detalle de las tareas')

# Load the Excel file
upload_excel = st.sidebar.file_uploader("Carga el archivo de excel", type=["xlsx"], accept_multiple_files=False)
database = None  # Initialize an empty DataFrame

# Load data if an Excel file is uploaded
if upload_excel:
    database = pd.read_excel(upload_excel, engine='openpyxl', sheet_name='Planeación General')
    def calculate_cumplimiento(row):
        if pd.notnull(row['Fecha de entrega real']):
            if row['Fecha de entrega real'] <= row['Fecha de entrega programada']:
                return 'si'
            else:
                return 'no'
        else:
            if datetime.datetime.now().date() > row['Fecha de entrega programada']:
                return 'no'
            else:
                return None

    database['Cumplimiento'] = database.apply(calculate_cumplimiento, axis=1)

    def calculate_estatus(row):
        if pd.notnull(row['Fecha de entrega real']):
            if row['Fecha de entrega real'] <= row['Fecha de entrega programada']:
                return 'si'
            else:
                return 'no'
        else:
            if datetime.datetime.now().date() > row['Fecha de entrega programada']:
                return 'no'
            else:
                return None

    database['Estatus'] = database.apply(calculate_estatus, axis=1)

    tab1, tab2 =st.tabs(['KPIs x Consutor', 'KPIs x Cliente'])

    with tab1:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if database is not None and not database.empty:
                filtro_consultor = st.selectbox(
                    "Selecciona al Consultor",
                    options=["Selecciona"] + list(database['Consultor'].unique())
                )
            else:
                filtro_consultor = st.selectbox(
                    "Selecciona al Consultor",
                    options=["Selecciona"]
                )
        kpis_consultor_fc = database[database['Consultor'] == filtro_consultor]

        with col2:
            if kpis_consultor_fc is not None and not kpis_consultor_fc.empty:
                filtro_consultor_sr = st.selectbox(
                    "Selecciona al Senior",
                    options=["Selecciona"] + list(kpis_consultor_fc['Consultor Sr'].unique())
                )
            else:
                filtro_consultor_sr = st.selectbox(
                    "Selecciona al Senior",
                    options=["Selecciona"]
                )


        kpis_consultor_fc_sr = kpis_consultor_fc[kpis_consultor_fc['Consultor Sr'] == filtro_consultor_sr]


        with col3:
            if kpis_consultor_fc_sr is not None and not kpis_consultor_fc_sr.empty:
                filtro_gerente = st.selectbox(
                    "Selecciona al Gerente",
                    options=["Selecciona"] + list(kpis_consultor_fc_sr['Gerente'].unique())
                )
            else:
                filtro_gerente = st.selectbox(
                    "Selecciona al Gerente",
                    options=["Selecciona"]
                )
        
        kpis_consultor_fc_sr_gt = kpis_consultor_fc_sr[kpis_consultor_fc_sr['Gerente'] == filtro_gerente]
        

        with col4:
            if kpis_consultor_fc_sr_gt is not None and not kpis_consultor_fc_sr_gt.empty:
                filtro_grupo = st.selectbox(
                    "Selecciona al Grupo Corporativo",
                    options=["Selecciona"] + list(kpis_consultor_fc_sr_gt['Grupo'].unique())
                )
            else:
                filtro_grupo = st.selectbox(
                    "Selecciona al Grupo Corporativo",
                    options=["Selecciona"]
                )


        kpis_consultor_fc_sr_gt_gp = kpis_consultor_fc_sr_gt[kpis_consultor_fc_sr_gt['Grupo'] == filtro_grupo]
        
        total_tareas = kpis_consultor_fc_sr_gt_gp['Cumplimiento'].count()
        tareas_cumplidas = len(kpis_consultor_fc_sr_gt_gp[kpis_consultor_fc_sr_gt_gp['Cumplimiento']=='si'])
        tareas_no_cumplidas = total_tareas - tareas_cumplidas
        pct_cumplimiento = (tareas_cumplidas/total_tareas)
        pct_cumplimiento = "{:.2%}".format(pct_cumplimiento)

        st.divider()
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Tareas Cumplidas", value=tareas_cumplidas) #, delta=tareas_no_cumplidas)

        with col2:
            st.metric(label="Total Tareas", value= total_tareas)

        with col3:
            st.metric(label="% Cumplimiento", value= pct_cumplimiento)

        with col4:
            st.metric(label="Tareas No Cumplidas", value= tareas_no_cumplidas)

        # resumen_kpis_emp = kpis_consultor_fc_sr_gt_gp.groupby(by=['Consultor'], as_index=False).agg({'Tiempo estimado de Actividad': 'sum','Tiempo Real': 'sum'})

        # st.dataframe(resumen_kpis_emp)                
        st.divider()
        st.write('Actividades')
        st.dataframe(kpis_consultor_fc_sr_gt_gp)


# import streamlit as st
# import pandas as pd
# import datetime


# st.set_page_config(
#     page_title="Base Firma",
#     page_icon="⏱",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'mailto:miguel.karim@karimortega.com'
#     }
# )

# # Load the Excel file
# data = pd.read_csv('database.csv')

# #sidebar menu & filters
# st.sidebar.image("BaseFirmaLogo.png", caption="Your Go-To Transfer Pricing Firm in the Americas")
# st.sidebar.header("Aplicar los filtros")
# filtro_clientes = st.sidebar.multiselect(
#     "Selecciona al Grupo Corporativo",
#     options = data['Cliente'].unique(),
#     default = data['Cliente'].unique(),
# )

# filtro_consultor = st.sidebar.multiselect(
#     "Selecciona al Consultor",
#     options = data['Consultor'].unique(),
#     default = data['Consultor'].unique(),
# )

# filtro_consultor_sr = st.sidebar.multiselect(
#     "Selecciona al Senior",
#     options = data['Senior'].unique(),
#     default = data['Senior'].unique(),
# )

# filtro_gerente = st.sidebar.multiselect(
#     "Selecciona al Gerente 1️⃣",
#     options = data['Gerente'].unique(),
#     default = data['Gerente'].unique(),
# )



# # st.image("BaseFirmaLogo.png", width=150)
# st.header('KPIs Dashboard')

#     #--settings--
# gerentes = ["Jaime Romero", "Karen Ramos"]
# consultores = ["Jorge Amaya", "Leslie Castillo", "Martin Rivera", "Rebeca Sandoval", "Sofia Vences", "Otro"] 
# consultores_sr = ["Brenda Salazar", "Christian Huitron", "Guillermo Pato"]
# grupos = ["CHUBB", "ACCIONA", "Crehana", "Corona", "Adabe Capital", "Luxottica", "Grupo IAMSA", "Melia"]
# sociedades = ["ABA Asistencias", "ABA Garantias SA de CV", "Acciona Agua Mexico S RL CV (AGUA)", "Acciona Energía México, S. de R.L. de C.V. (ENERGIA)", "Acciona Energía Servicios México, S. de R.L. de C.V. (ENERGIA)", "Acciona Eólica Santa Cruz S. R.L. de C.V. (ENERGIA)"
#               "Acciona Forwarding (SERVICES)", "Acciona Infraestructuras México, S.A. de C.V. (INFRAESTRUCTURA)", "Acciona Infraestructuras Residenciales México, S.A. de C.V. (INFRAESTRUCTURA)"]



# # Display the updated data in a dataframe
# st.write("Updated Data:")

# kpis_empleado = pd.DataFrame(data)

# kpis_empleado = data.query(
#     "Cliente in @filtro_clientes & Consultor in @filtro_consultor & Senior in @filtro_consultor_sr & Gerente in @filtro_gerente"
# )
# total_tareas = kpis_empleado['Cumplio'].count()
# tareas_cumplidas = len(kpis_empleado[kpis_empleado['Cumplio']=='Si'])
# tareas_no_cumplidas = total_tareas - tareas_cumplidas
# pct_cumplimiento = (tareas_cumplidas/total_tareas)
# pct_cumplimiento = "{:.2%}".format(pct_cumplimiento)

# col1, col2, col3, col4 = st.columns(4)
# with col1:
#     st.metric(label="Tareas Cumplidas", value=tareas_cumplidas) #, delta=tareas_no_cumplidas)

# with col2:
#     st.metric(label="Total Tareas", value= total_tareas)

# with col3:
#     st.metric(label="% Cumplimiento", value= pct_cumplimiento)

# with col4:
#     st.metric(label="Tareas No Cumplidas", value= tareas_no_cumplidas)

# resumen_kpis_emp = kpis_empleado.groupby(by=['Consultor'], as_index=False).agg({'Tiempo estimado de Actividad': 'sum','Tiempo Real': 'sum'})

# # st.dataframe(resumen_kpis_emp)                

# tab1, tab2, tab3, tab4 = st.tabs(["Alta Registro", "KPIs por Empleado", "KPIs Por Proyecto", "Data"])

# with tab1:
#     st.subheader("Alta de nuevo registro")
#     # Create a form to create a new record
#     with st.form("Create new record", clear_on_submit=True):
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             cliente = st.selectbox("Seleciona al Grupo:", grupos)
#             sociedad = st.selectbox("Seleciona la entidad legal:", sociedades)
#             proyecto = st.text_input("Proyecto")
        
#         with col2:
#             consultor = st.selectbox("Seleciona al Consultor:", consultores)
#             senior = st.selectbox("Seleciona al Consultor Sr:", consultores_sr)
#             gerente = st.selectbox("Seleciona al Gerente:", gerentes)
    
#         with col3:
#             tiempo_est = st.number_input("Horas Estimadas")
#             tiempo_real = st.number_input("Horas Reales")
#             fecha_est = st.date_input("Fecha Estimada de Entrega", datetime.date(2023,1,1))
#             fecha_real = st.date_input("Fecha Real de Entrega", datetime.date(2023,1,1))
    
#         submit_button = st.form_submit_button(label='Add Record')
    
#     # If the form is submitted, add the new record to the DataFrame
#     if submit_button:
#         new_record = {"Cliente": cliente, "Sociedad": sociedad, "Proyecto": proyecto, "Consultor": consultor, "Senior": senior, "Gerente": gerente, "Tiempo estimado de Actividad": tiempo_est, "Fecha Planeada": fecha_est,
#                      "Fecha de entrega efectiva": fecha_real, "Tiempo Real": tiempo_real}
#         new_row = pd.DataFrame([new_record])
#         data = pd.concat([data, new_row], ignore_index=True)
#         # Save the updated DataFrame to the CSV file
#         data.to_csv('database.csv', index=False)
    

# with tab2:
#     st.subheader("KPI's por empleado")
#     st.dataframe(kpis_empleado)
# with tab3:
#     st.subheader("KPI's por Proyecto")
# with tab4:
#     # Display the data in a dataframe
#     with st.expander("Tabla"):
#         st.dataframe(data)







# # st.dataframe(data)
