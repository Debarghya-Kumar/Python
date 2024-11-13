#Write a python program to merge two dictionaries into one. The values of the same keys should multiply. Use user defined functions. 

def merge_dicts_multiply_values(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of dict1

    for key, value in dict2.items():
        if key in merged_dict:
            # Multiply the values if key exists in both dictionaries
            merged_dict[key] *= value
        else:
            # Add the key-value pair if it doesn't exist in dict1
            merged_dict[key] = value

    return merged_dict

# Example usage:
dict1 = {'a': 2, 'b': 3, 'c': 4}
dict2 = {'b': 5, 'c': 6, 'd': 7}

result = merge_dicts_multiply_values(dict1, dict2)
print(result)
