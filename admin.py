import streamlit as st
import pandas as pd


# Load the Excel file

data = pd.read_excel('database.xlsx',  sheet_name = 'Data', engine='openpyxl')

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
