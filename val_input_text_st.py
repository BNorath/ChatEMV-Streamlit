# use this function to validate length and permissable characters user input
# in st.text_input

import streamlit as st

hex_check = "0123456789abcdef"

def validate_input():
    input_str = st.session_state.input_value
    # Allowed characters are hexadecimal characters
    allowed_chars = set(hex_check)
    for char in input_str:
        if char not in allowed_chars:
            st.warning("Value may only have characters between 0-9 and a-f")
            return
    # Must be exactly 10 characters long
    if len(input_str) != 10:
        st.warning("Please enter exactly 10 characters.")
        return
    st.success("Yes! This is a valid value.")

def validate_input_2B():
    input_str = st.session_state.input_value
    # Allowed characters are hexadecimal characters
    allowed_chars = set(hex_check)
    for char in input_str:
        if char not in allowed_chars:
            st.warning("Value may only have characters between 0-9 and a-f")
            return
    # Must be exactly 4 characters long
    if len(input_str) != 4:
        st.warning("Please enter exactly 4 characters.")
        return
    st.success("Yes! This is a valid value.")

