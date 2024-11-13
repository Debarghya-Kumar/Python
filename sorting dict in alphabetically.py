#Write a python program to sort the keys of a dictionary in alphabetical order. Use user defined functions.

def sort_dict_keys_alphabetically(input_dict):
    # Sort the dictionary keys in alphabetical order
    sorted_dict = {key: input_dict[key] for key in sorted(input_dict)}
    return sorted_dict

# Example usage:
my_dict = {'banana': 3, 'apple': 4, 'cherry': 1, 'date': 2}

result = sort_dict_keys_alphabetically(my_dict)
print(result)
