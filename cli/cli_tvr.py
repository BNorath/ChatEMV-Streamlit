from hex_2_bin import hex_2_bin
from str_2_dict import update_dict
import pandas


hex_check = "0123456789abcdef"

while True:
    hex_input = (input("Enter 5 byte hex value: ")).lower()

    if len(hex_input) != 10:
        print("TVR value must be 5 Bytes long.(10 characters)")

    elif not all(c in hex_check for c in hex_input):
        print("Please re-enter TVR value, Valid characters are between 0-9 and a-f.")

    else:
        break

# convert hex string to binary string
bin_output = hex_2_bin(hex_input)
print(bin_output)

# write string to a dictionary
new_dict = update_dict(bin_output)
#print(new_dict)

print(f"The following bits are set to true in the transaction:")
maplist = []
for key, val in new_dict.items():
    if val == "1":
        #print(key)
        maplist.append(key)
print(maplist)

df = pandas.read_csv("tvr_map.csv")

new_df = df[df['bytebit'].isin(pandas.Series(maplist))]

for index, row in new_df.iterrows():
    print(row["bytebit"])
    print(row["notes"])

# in web version use maplist to select tickboxes





##### confirm if csv files must have "" around the values






