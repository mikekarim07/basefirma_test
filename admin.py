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


st.image("https://basefirma.com/wp-content/uploads/2022/02/BaseFirma-LogoColor-2048x850.png", width=150)
st.write('hello world l')
# Load the Excel file

data = pd.read_csv('database.csv')

st.dataframe(data)

# # Create a form to create a new record
# st.form("Create new record")
# name = st.text_input("Name")
# email = st.text_input("Email")

# # If the form is submitted, add the new record to the Excel file
# if st.form_submitted():
#     data = data.append({"Name": name, "Email": email}, ignore_index=True)
#     data.to_excel(excel_file)

# # Display the data in a dataframe
# st.dataframe(data)
