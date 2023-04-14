import streamlit as st

# Configure page to resize
st.set_page_config(layout="wide")

# Add page title
st.title("About ChatEMV")

# Add a summary
st.write("")
st.write("""
This site is a work in progress and is part of my journey towards mastering 
Python. \n

This version is written in core Python, using the STREAMLIT library to render the
  webpages. My current knowledge of STREAMLIT is very basic, and this reflects
  in the quality of the webpages. LOL, I will get there eventually.\n

I hope to do more versions of this website later on using frameworks like 
FLASK and DJANGO, but that's a discussion for another day.
""")

link='If you would like to learn more about EMV, please check out my YouTube ' \
     'training [link](https://www.youtube.com/playlist?' \
     'list=PLoS9InuPCEh5-i2R2ZwU1wAjebq9mccJu)'
st.markdown(link, unsafe_allow_html=True)

link='Please find the source code for this website in my Github repository [link]' \
     '(https://github.com/BNorath/ChatEMV-Streamlit.git)'
st.markdown(link, unsafe_allow_html=True)










