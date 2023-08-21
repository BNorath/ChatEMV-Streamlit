

import streamlit as st
import pandas as pd

# Configure page to resize
st.set_page_config(layout="wide")

# Add page title
st.title("ChatEMV")

# Add a summary
st.write("")
st.write("""
Welcome to my site where we discuss all things EMV. \n

This is a work in progress so please bear with me. I will slowly add more 
functionality over time. Whilst every effort has been made to use the current
versions of the various EMV tags, there is no guarantee that I wil be able to 
update the tags timeously as and when they change. For this reason, please 
ensure that you verify that the checklists on the site is in line with the 
latest technical specifications, especially if you are using this site to 
support your EMV delivery or testing. I cannot be held liable for any errors 
or outdated specifications that may be present on this site. \n

If you are on a web browser on a computer/laptop, you will see the translators
listed below appearing on separate pages on the left hand menu.\n
 
If you are accessing the site using a web browser on a mobile device, please
click on the > symbol on the upper left hand corner of the screen to access the 
full list of available translators listed below. \n
""")
st.write("")

# list all available translators by reading translators.csv file.
df = pd.read_csv("files/translators.csv")
df_sorted = df.sort_values("acron")
for index, row in df_sorted.iterrows():
    acron = (row['acron'])
    tag = (row['tag'])
    name = (row['name'])
    desc = (row['description'])
    st.subheader(f"{name} - {acron} {tag}")
    st.write(desc)
    st.write("")







