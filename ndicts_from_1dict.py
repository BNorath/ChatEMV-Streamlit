# Create multiple smaller dictionaries from 1 big dictionary

def create_new_dict(original_dict, start_index, end_index):
    new_dict = {}
    keys = list(original_dict.keys())[start_index:end_index+1]
    for key in keys:
        new_dict[key] = original_dict[key]
    return new_dict

# use the following calls in main to split main dict by every 8 items

# dict1 = create_new_dict(desc_dict, 0, 7)
# dict2 = create_new_dict(desc_dict, 8, 15)
# dict3 = create_new_dict(desc_dict, 16, 23)
# dict4 = create_new_dict(desc_dict, 24, 31)
# dict5 = create_new_dict(desc_dict, 32, 39)
