import streamlit as st
import pandas as pd

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


st.dataframe(data)

# Create a form to create a new record
st.form("Create new record")
cliente = st.text_input("Cliente")
sociedad = st.text_input("Razon Social")

# If the form is submitted, add the new record to the Excel file
if st.form_submitted():
    data = data.append({"Cliente": cliente, "Sociedad": sociedad}, ignore_index=True)
    data.to_csv(data)

# Display the data in a dataframe
st.dataframe(data)
