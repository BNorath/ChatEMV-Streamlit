from hex_2_bin import hex_2_bin
from str_2_dict import update_dict


hex_input = input("Enter 5 byte hex value: ")

# convert hex string to binary string
bin_output = hex_2_bin(hex_input)
print(bin_output)

# write string to a dictionary
new_dict = update_dict(bin_output)
print(new_dict)

print(f"The following bits are set to true in the transaction:")
maplist = []
for key, val in new_dict.items():
    if val == "1":
        print(key)
        maplist.append(key)
print(maplist)



##### confirm if csv files must have "" around the values





# create dict with indexes and values for each byte, then display the keys where value == 1 to print in order desc
# see code in notes
# store the dictionaries in script or in json file?




