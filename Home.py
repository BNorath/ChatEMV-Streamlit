

import streamlit as st
import pandas

# Configure page to resize
st.set_page_config(layout="wide")

# Add page title
st.title("ChatEMV")

# Add a summary
st.write("")
st.write("""
Welcome to my site where we discuss all things EMV. \n

This is a work in progress so please bear with me. I will slowly add more 
functionality over time. \n

At this point in time we have the following translators available: \n
(They can be found as separate pages in the menu on the left)
""")

# list all available translators by reading translators.csv file.
df = pandas.read_csv("translators.csv")
for index, row in df.iterrows():
    acron = (row['acron'])
    tag = (row['tag'])
    name = (row['name'])
    desc = (row['description'])
    st.subheader(f"{acron} - {tag}")
    st.write(desc)






