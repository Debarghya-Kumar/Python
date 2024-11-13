def union_of_lists(list1, list2):
    # Use set union to get unique elements from both lists
    return list(set(list1) | set(list2))

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_of_lists(list1, list2)
print(result)
