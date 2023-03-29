from string_rev import reverse

hex_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
            '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
            'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

hex_input = input("Enter 5 byte hex value: ")

bin_output = ''
for digit in hex_input:
    bin_output += hex_dict[digit]
print(bin_output)


byte1 = reverse(bin_output[0:8])
byte2 = reverse(bin_output[8:16])
byte3 = reverse(bin_output[16:24])
byte4 = reverse(bin_output[24:32])
byte5 = reverse(bin_output[32:40])

print("Byte 1: ", byte1)
print("Byte 2: ", byte2)
print("Byte 3: ", byte3)
print("Byte 4: ", byte4)
print("Byte 5: ", byte5)

b1_dict = {"Byte1_bit8": "", "Byte1_bit7": "", "bit6": "", "bit5": "", "bit4": "", "bit3": "", "bit2": "", "bit1": ""}
for i in string(): # for each char in string, add in sequence to dict.






for index, bit in enumerate(byte1):
    if bit == "1":
        print(f" Byte 3, bit {index +1}")

# create dict with indexes and values for each byte, then display the keys where value == 1 to print in order desc



