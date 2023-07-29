import streamlit as st
import pandas as pd
import xlrd

# Load the Excel file
excel_file = "data.xlsx"
data = pd.read_excel(excel_file)

# Create a form to create a new record
st.form("Create new record")
name = st.text_input("Name")
email = st.text_input("Email")

# If the form is submitted, add the new record to the Excel file
if st.form_submitted():
    data = data.append({"Name": name, "Email": email}, ignore_index=True)
    data.to_excel(excel_file)

# Display the data in a dataframe
st.dataframe(data)
