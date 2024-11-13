#WAP to find the intersection of two dictionaries using a function.
def intersect_dicts(dict1, dict2):
    # Find intersection by retaining common key-value pairs
    return {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

result = intersect_dicts(dict1, dict2)
print(result)  
