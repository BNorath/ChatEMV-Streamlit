
import streamlit as st


st.set_page_config(layout="wide")


st.title("EMV Interpreter")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.write("Please enter a 5 Byte EMV value:")


with col2:
    hex_input = st.text_input(label=" ", placeholder="5 Bytes or 10 characters")
    bin_val =

                  #on_change=,
                  #key="new_todo"


st.write("This translates into the following binary value:")
# convert hex to binary and display result - separate the Bytes
st.write(bin_val)

st.write("Only the bits set to 1 are relevant, so let's focus on the following bits:")
# show only the relevant bitsets in format Bnbn

st.write("""
According to the terminal's view of the transaction, the following events occurred: """)
# compare relevant bitsets above to TVR checksheet and display matching items




