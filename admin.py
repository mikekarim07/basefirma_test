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

# Display the data in a dataframe
st.dataframe(data)

# Create a form to create a new record
with st.form("Create new record"):
    cliente = st.text_input("Cliente")
    sociedad = st.text_input("Razon Social")
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
