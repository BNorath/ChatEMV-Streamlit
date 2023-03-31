# this function will write the string to a pre-defined dictionary

my_dict = {"Byte1 bit8": "", "Byte1 bit7": "", "Byte1 bit6": "",
           "Byte1 bit5": "", "Byte1 bit4": "", "Byte1 bit3": "",
           "Byte1 bit2": "", "Byte1 bit1": "", "Byte2 bit8": "",
           "Byte2 bit7": "", "Byte2 bit6": "", "Byte2 bit5": "",
           "Byte2 bit4": "", "Byte2 bit3": "", "Byte2 bit2": "",
           "Byte2 bit1": "", "Byte3 bit8": "", "Byte3 bit7": "",
           "Byte3 bit6": "", "Byte3 bit5": "", "Byte3 bit4": "",
           "Byte3 bit3": "", "Byte3 bit2": "", "Byte3 bit1": "",
           "Byte4 bit8": "", "Byte4 bit7": "", "Byte4 bit6": "",
           "Byte4 bit5": "", "Byte4 bit4": "", "Byte4 bit3": "",
           "Byte4 bit2": "", "Byte4 bit1": "", "Byte5 bit8": "",
           "Byte5 bit7": "", "Byte5 bit6": "", "Byte5 bit5": "",
           "Byte5 bit4": "", "Byte5 bit3": "", "Byte5 bit2": "",
           "Byte5 bit1": ""}


def update_dict(string):
    for i, char in enumerate(string):
        my_dict[list(my_dict.keys())[i]] = char

    return my_dict

