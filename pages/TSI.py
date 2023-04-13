
import streamlit as st
import pandas as pd
from hex_2_bin import hex_2_bin
from string_csv_2_dict import create_dict
from ndicts_from_1dict import create_new_dict
from val_input_text_st import validate_input_2B

# Declare global variables
bin_output = "0000000000000000"
hex_input = ""
relevant_dict = {}

# Configure page to dynamically resize
st.set_page_config(layout="wide")

# Title of page
st.title("TSI Translator")

# Use columns to reduce width of input box
col1, col2, col3 = st.columns(3)
with col1:
    hex_val = st.text_input("Please enter a 2 Byte TSI value:",
                            placeholder="Enter 4 characters, valid characters are 0-9 and a-f ",
                            key="input_value",
                            on_change=validate_input_2B,
                            max_chars=4)
    if not hex_val:
        hex_val = "0000"

# Convert all to lower case so that comparison against check_value works
if hex_val:
    hex_input = hex_val.lower()
# Convert to binary
if hex_input != "0000":
    st.write("")
    st.write("")
    st.write("This translates into the following binary value:")
    bin_output = hex_2_bin(hex_input)
    #print(bin_output)
    st.subheader(bin_output)

# Create new dict from tvr_map.csv and bin_output using create_dict function
    string = bin_output
    csv_file = "files/tsi_map.csv"
    full_dict = create_dict(csv_file, string)
    #print(full_dict)

# Produce new dictionary with key=bytebit, value = 1
    for i, v in full_dict.items():
        relevant_dict = {key: value for key, value in full_dict.items() if value == "1"}

# create dataframe from full TVR map csv doc
df = pd.read_csv('files/tsi_map.csv')

# Produce single dict with full descriptions for Checkboxes
desc_dict = {}
for index, row in df.iterrows():
    desc_dict[row['bytebit']] = row['description']

# Split single dictionary into smaller dict per checkbox column
dict1 = create_new_dict(desc_dict, 0, 7)
dict2 = create_new_dict(desc_dict, 8, 15)
#dict3 = create_new_dict(desc_dict, 16, 23)
#dict4 = create_new_dict(desc_dict, 24, 31)
#dict5 = create_new_dict(desc_dict, 32, 39)

if hex_input != "0000":
    st.write("")
    st.write("")
    st.write("The following TVR bits are set to True in this transaction:")

# create 5 columns, 1 per byte.
col1, col2 = st.columns(2)

# create 1 checkbox per bit in each byte/column
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


if hex_input != "0000":
    st.subheader("In simpler terms, the following events happened during this transaction:")


notes_dict = {}
for index, row in df.iterrows():
    if row['bytebit'] in relevant_dict:
        notes_dict[row['bytebit']] = row['notes']

for key, value in notes_dict.items():
    st.write(key)
    st.write(value)




