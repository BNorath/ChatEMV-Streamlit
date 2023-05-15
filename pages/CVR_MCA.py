
import streamlit as st
import pandas as pd
from hex_2_bin import hex_2_bin
from ndicts_from_1dict import create_new_dict
from val_input_text_st import validate_input_6b


# Declare global variables
bin_output = "000000000000000000000000000000000000000000000000"
hex_input = ""
relevant_dict1 = {}
relevant_dict2 = {}
relevant_dict3 = {}
relevant_dict4 = {}
relevant_dict5 = {}
relevant_dict6 = {}
csv_file = "files/cvr_mca.csv"
df = pd.read_csv(csv_file)

# Configure page to dynamically resize
st.set_page_config(layout="wide")

# Title of page
st.title("CVR Translator for MChip Advance")

# Use columns to reduce width of input box
col1, col2, col3 = st.columns(3)
with col1:
    hex_val = st.text_input("Please enter a 6 Byte CVR value:",
                            placeholder="Enter 12 characters, valid characters are 0-9 and a-f ",
                            key="input_value",
                            on_change=validate_input_6b,
                            max_chars=12)
    if not hex_val:
        hex_val = "000000000000"

# Convert all to lower case so that comparison against check_value works
if hex_val:
    hex_input = hex_val.lower()
# Convert to binary
if hex_input != "000000000000":
    byte1 = hex_input[0:2]
    byte2 = hex_input[2:4]
    byte3 = hex_input[4:6]
    byte4 = hex_input[6:8]
    byte5 = hex_input[8:10]
    byte6 = hex_input[10:12]

    byte1_bin = hex_2_bin(byte1)
    byte1_87 = byte1_bin[0:2]
    byte1_65 = byte1_bin[2:4]
    byte1_rem = byte1_bin[4:8]

    byte2_bin = hex_2_bin(byte2)

    byte3_bin = hex_input[4:6]
    byte3_85 = hex_input[4]
    byte3_41 = hex_input[5]
    byte3_85_dec = str(int(byte3_85, 16))
    byte3_41_dec = str(int(byte3_41, 16))

    byte4_bin = hex_2_bin(byte4)
    byte5_bin = hex_2_bin(byte5)
    byte6_bin = hex_2_bin(byte6)

    st.write("")
    st.write("")
    st.write("This translates into the following values:")
    st.write(f"The binary value of Byte 1 = {byte1_bin}")
    st.write(f"The binary value of Byte 2 = {byte2_bin}")
    st.write(f"The decimal value of Byte 3, bits 8 to 5 = {byte3_85_dec}")
    st.write(f"The decimal value of Byte 3, bits 4 to 1 = {byte3_41_dec}")
    st.write(f"The binary value of Byte 4 = {byte4_bin}")
    st.write(f"The binary value of Byte 5 = {byte5_bin}")
    st.write(f"The binary value of Byte 6 = {byte6_bin}")


# create Byte 1 dictionary
    dict_b1 = {}

    # iterate over the rows in the dataframe for bits8+7
    for index, row in df[0:4].iterrows():
        # check if the 2-character string matches the bval column value
        if row["bval"] == byte1_87:
            # if there's a match, add the bytebit column value as a key to the
            # dictionary with a value of 1
            dict_b1[row["bytebit"]] = "1"
        else:
            dict_b1[row["bytebit"]] = "0"

    # iterate over the rows in the dataframe for bits 6+5
    for index, row in df[4:8].iterrows():
        # check if the 2-character string matches the bval column value
        if row["bval"] == byte1_65:
            # if there's a match, add the bytebit column value as a key to the
            # dictionary with a value of 1
            dict_b1[row["bytebit"]] = "1"
        else:
            dict_b1[row["bytebit"]] = "0"

    # iterate over the rows in the dataframe for bits 4 - 1
    new_list = [char for char in byte1_rem]
    for index, row in df[8:12].iterrows():
        dict_b1[row["bytebit"]] = new_list[0]
        new_list.pop(0)


# Create Byte 2 dictionary
    dict_b2 = {}
    b2_list = [char for char in byte2_bin]
    for index, row in df[12:20].iterrows():
        dict_b2[row["bytebit"]] = b2_list[0]
        b2_list.pop(0)

# Create Byte 3 dictionary
    dict_b3 = {}
    b3_list = [byte3_85_dec, byte3_41_dec]
    for index, row in df[20:22].iterrows():
        dict_b3[row["bytebit"]] = b3_list[0]
        b3_list.pop(0)

# Create Byte 4 dictionary
    dict_b4 = {}
    b4_list = [char for char in byte4_bin]
    for index, row in df[22:30].iterrows():
        dict_b4[row["bytebit"]] = b4_list[0]
        b4_list.pop(0)

# Create Byte 5 dictionary
    dict_b5 = {}
    b5_list = [char for char in byte5_bin]
    for index, row in df[30:38].iterrows():
        dict_b5[row["bytebit"]] = b5_list[0]
        b5_list.pop(0)

# Create Byte 6 dictionary
    dict_b6 = {}
    b6_list = [char for char in byte6_bin]
    for index, row in df[38:46].iterrows():
        dict_b6[row["bytebit"]] = b6_list[0]
        b6_list.pop(0)

# Produce new dictionary with key=bytebit, value = 1

    for key, value in dict_b1.items():
        relevant_dict1 = {key: value for key, value in dict_b1.items() if
                          value == "1"}

    for key, value in dict_b2.items():
        relevant_dict2 = {key: value for key, value in dict_b2.items() if
                          value == "1"}

    for key, value in dict_b3.items():
        relevant_dict3 = {key: value for key, value in dict_b3.items() if
                          value != "X"}

    for key, value in dict_b4.items():
        relevant_dict4 = {key: value for key, value in dict_b4.items() if
                          value == "1"}

    for key, value in dict_b5.items():
        relevant_dict5 = {key: value for key, value in dict_b5.items() if
                          value == "1"}

    for key, value in dict_b6.items():
        relevant_dict6 = {key: value for key, value in dict_b6.items() if
                          value == "1"}

# Produce single dict with full descriptions for Checkboxes
desc_dict = {}
for index, row in df.iterrows():
    desc_dict[row['bytebit']] = row['description']


# Split single dictionary into smaller dict per checkbox column
dict1 = create_new_dict(desc_dict, 0, 11)
dict2 = create_new_dict(desc_dict, 12, 19)
dict3 = create_new_dict(desc_dict, 19, 21)
dict4 = create_new_dict(desc_dict, 22, 29)
dict5 = create_new_dict(desc_dict, 30, 37)
dict6 = create_new_dict(desc_dict, 38, 46)


if hex_input != "000000000000":
    st.write("")
    st.write("")
    st.write("The following CVR bits are set to True in this transaction:")

# create 3 columns, 1 per byte.
col1, col2, col3 = st.columns(3)

# create 1 checkbox per bit in each byte/column
with col1:
    st.subheader("Byte 1")
    for index, value in dict1.items():
        checkbox_value = False
        for key in relevant_dict1.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[0:15]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col2:
    st.subheader("Byte 2")
    for index, value in dict2.items():
        checkbox_value = False
        for key in relevant_dict2.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[0:15]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col3:
    st.subheader("Byte 3")
    if hex_input == "000000000000":
        st.write(f"Bits 8-5 indicate the right nibble of the script counter.")
        st.write(f"Bits 4-1 indicate the right nibble of the Pin Try counter.")

    if hex_input != "000000000000":
        st.write(f"The Right nibble of the script counter = {byte3_85_dec}")
        st.write(f"The Right nibble of the Pin Try counter = {byte3_41_dec}")

# create 3 columns, 1 per byte.
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Byte 4")
    for index, value in dict4.items():
        checkbox_value = False
        for key in relevant_dict4.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[0:15]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)

with col5:
    st.subheader("Byte 5")
    for index, value in dict5.items():
        checkbox_value = False
        for key in relevant_dict5.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[0:15]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)
with col6:
    st.subheader("Byte 6")
    for index, value in dict6.items():
        checkbox_value = False
        for key in relevant_dict6.keys():
            if index == key:
                checkbox_value = True
                break
        st.checkbox(label=(f"{index[0:15]}: {value}"),
                    value=checkbox_value,
                    disabled=True,
                    key=index)


if hex_input != "000000000000":
    st.subheader("In simpler terms, the following events happened during this "
                 "transaction:")


notes_dict = {}
for index, row in df.iterrows():
    if row['bytebit'] in relevant_dict1:
        notes_dict[row['bytebit']] = row['notes']
    if row['bytebit'] in relevant_dict2:
        notes_dict[row['bytebit']] = row['notes']
    if row['bytebit'] in relevant_dict3:
        notes_dict[row['bytebit']] = row['notes']
    if row['bytebit'] in relevant_dict4:
        notes_dict[row['bytebit']] = row['notes']
    if row['bytebit'] in relevant_dict5:
        notes_dict[row['bytebit']] = row['notes']
    if row['bytebit'] in relevant_dict6:
        notes_dict[row['bytebit']] = row['notes']

for key, value in notes_dict.items():
    if key == "Byte3 bit8to5":
        st.write(key)
        st.write(f"{byte3_85_dec} {value}")
    elif key == "Byte3 bit4to1":
        st.write(key)
        st.write(f"{byte3_41_dec} {value}")
    else:
        st.write(key)
        st.write(value)



