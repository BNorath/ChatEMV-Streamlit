
import streamlit as st
import pandas as pd
from hex_2_bin import hex_2_bin
from str_2_dict import update_dict
from ndicts_from_1dict import create_new_dict
from val_input_text_st import validate_input

bin_output = ""

# Configure page to dynamically resize
st.set_page_config(layout="wide")

# Title of page
st.title("TVR Translator")

# Use columns to reduce width of input box
col1, col2, col3 = st.columns(3)
with col1:
    hex_val = st.text_input("Please enter a 5 Byte TVR value:",
                            placeholder="Enter 10 characters, valid characters are 0-9 and a-f ",
                            key="input_value",
                            on_change=validate_input,
                            max_chars=10)

# Convert all to lower case so that comparison against check_value works
hex_input = hex_val.lower()

# Check if hex is 5 bytes long and then convert to binary
if len(hex_input) == 10:
    st.write("")
    st.write("")
    st.write("This translates into the following binary value:")
    bin_output = hex_2_bin(hex_input)
    st.subheader(bin_output)

# Create new dict using existing dict with keys and new values
full_dict = update_dict(bin_output)

# Produce new dictionary with key=bytebit, value = 1
relevant_dict = {}
for i, v in full_dict.items():
    relevant_dict = {key: value for key, value in full_dict.items() if value == "1"}

# create dataframe from full TVR map csv doc
df = pd.read_csv('tvr_map.csv')

# Produce new dict with key = bytebit, value = description for display at end
for index, row in df.iterrows():
    if row['bytebit'] in relevant_dict:
        relevant_dict[row['bytebit']] = row['description']

# Produce single dict with full descriptions for Checkboxes
desc_dict = {}
for index, row in df.iterrows():
    desc_dict[row['bytebit']] = row['description']

# Split single dictionary into smaller dict per checkbox column
dict1 = create_new_dict(desc_dict, 0, 7)
dict2 = create_new_dict(desc_dict, 8, 15)
dict3 = create_new_dict(desc_dict, 16, 23)
dict4 = create_new_dict(desc_dict, 24, 31)
dict5 = create_new_dict(desc_dict, 32, 39)

if len(hex_input) == 10:
    st.write("")
    st.write("")
    st.write("The following TVR bits are set to True in this transaction:")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.subheader("Byte 1")
    for index, value in dict1.items():
        checkbox_value = False
        for key in relevant_dict.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[5:10]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)



with col2:
    st.subheader("Byte 2")
    for index, value in dict2.items():
        checkbox_value = False
        for key in relevant_dict.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[5:10]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col3:
    st.subheader("Byte 3")
    for index, value in dict3.items():
        checkbox_value = False
        for key in relevant_dict.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[5:10]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col4:
    st.subheader("Byte 4")
    for index, value in dict4.items():
        checkbox_value = False
        for key in relevant_dict.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[5:10]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col5:
    st.subheader("Byte 5")
    for index, value in dict5.items():
        checkbox_value = False
        for key in relevant_dict.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[5:10]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

if len(hex_input) == 10:
    st.subheader("In simpler terms, the following events happened during this transaction:")

notes_dict = {}
for index, row in df.iterrows():
    if row['bytebit'] in relevant_dict:
        notes_dict[row['bytebit']] = row['notes']

for key, value in notes_dict.items():
    st.write(key)
    st.write(value)




