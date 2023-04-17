from hex_2_bin import hex_2_bin
from string_csv_2_dict import create_dict
import pandas as pd


hex_check = "0123456789abcdef"

while True:
    hex_input = (input("Enter 2 byte hex value: ")).lower()

    if len(hex_input) != 4:
        print("AUC value must be 2 Bytes long.(4 characters)")

    elif not all(c in hex_check for c in hex_input):
        print("Please re-enter AUC value, Valid characters are between 0-9 and a-f.")

    else:
        break

# convert hex string to binary string
bin_output = hex_2_bin(hex_input)
print(bin_output)

# write string to a dictionary
string = bin_output
csv_file = "../files/auc_map.csv"
column_name = "bytebit"
new_dict = create_dict(csv_file, string)
#print(new_dict)

print(f"The following settings are configured to True on the card:")
maplist = []
for key, val in new_dict.items():
    if val == "1":
        #print(key)
        maplist.append(key)
#print(maplist)

df = pd.read_csv(csv_file)

new_df = df[df['bytebit'].isin(pd.Series(maplist))]

for index, row in new_df.iterrows():
    print(row["bytebit"])
    print(row["notes"])

