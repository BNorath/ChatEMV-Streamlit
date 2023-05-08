from hex_2_bin import hex_2_bin
from string_csv_2_dict import create_dict
import pandas as pd


hex_check = "0123456789abcdef"
csv_file = "../files/cvr_mca.csv"
df = pd.read_csv(csv_file)

while True:
    hex_input = (input("Enter 6 byte hex value: ")).lower()

    if len(hex_input) != 12:
        print("CVR value must be 6 Bytes long.(12 characters)")

    elif not all(c in hex_check for c in hex_input):
        print("Please re-enter CVR value, Valid characters are between 0-9 "
              "and a-f.")

    else:
        break

# convert hex string to binary string
byte1 = hex_input[0:2]
byte1_full = hex_2_bin(byte1)
byte1_87 = byte1_full[0:2]
byte1_65 = byte1_full[2:4]
byte1_rem = byte1_full[4:8]

byte2 = hex_input[2:4]
byte2_full = hex_2_bin(byte2)

# convert from hex to decimal
byte3 = hex_input[4:6]
byte3_85 = hex_input[4]
byte3_41 = hex_input[5]
byte3_85_dec = str(int(byte3_85, 16))
byte3_41_dec = str(int(byte3_41, 16))

# convert hex string to binary string
byte4 = hex_input[6:8]
byte4_full = hex_2_bin(byte4)

byte5 = hex_input[8:10]
byte5_full = hex_2_bin(byte5)

byte6 = hex_input[10:12]
byte6_full = hex_2_bin(byte6)

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
# print(f" Byte 1 full dict= {dict_b1}")

# string to dict for byte 2
dict_b2 = {}
b2_list = [char for char in byte2_full]
for index, row in df[12:20].iterrows():
    dict_b2[row["bytebit"]] = b2_list[0]
    b2_list.pop(0)
# print(dict_b2)

# Add byte 3 calc for decimal
dict_b3 = {}
b3_list = [byte3_85_dec, byte3_41_dec]
for index, row in df[20:22].iterrows():
    dict_b3[row["bytebit"]] = b3_list[0]
    b3_list.pop(0)
# print(dict_b3)

# continue string to dict for bytes 4-6
dict_b4 = {}
b4_list = [char for char in byte4_full]
for index, row in df[22:30].iterrows():
    dict_b4[row["bytebit"]] = b4_list[0]
    b4_list.pop(0)
# print(dict_b4)

dict_b5 = {}
b5_list = [char for char in byte5_full]
for index, row in df[30:38].iterrows():
    dict_b5[row["bytebit"]] = b5_list[0]
    b5_list.pop(0)
# print(dict_b5)

dict_b6 = {}
b6_list = [char for char in byte6_full]
for index, row in df[38:46].iterrows():
    dict_b6[row["bytebit"]] = b6_list[0]
    b6_list.pop(0)
# print(dict_b6)

print(f"The following bits are set to true in the transaction:")
maplist = []
for key, val in dict_b1.items():
    if val == "1":
        maplist.append(key)

for key, val in dict_b2.items():
    if val == "1":
        maplist.append(key)

for key, val in dict_b3.items():
    maplist.append(key)

for key, val in dict_b4.items():
    if val == "1":
        maplist.append(key)

for key, val in dict_b5.items():
    if val == "1":
        maplist.append(key)

for key, val in dict_b6.items():
    if val == "1":
        maplist.append(key)

# print(maplist)

new_df = df[df['bytebit'].isin(pd.Series(maplist))]

for index, row in new_df.iterrows():
    if row["bytebit"] == "Byte3 bit8to5":
        print(row["bytebit"])
        print(byte3_85_dec, row["notes"])
    elif row["bytebit"] == "Byte3 bit4to1":
        print(row["bytebit"])
        print(byte3_41_dec, row["notes"])

    else:
        print(row["bytebit"])
        print(row["notes"])
