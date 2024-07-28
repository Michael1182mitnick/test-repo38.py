# Write a Python program to merge two lists into a single list.

def merge_list(list1, list2):
    merged_list = list1 + list2
    return merged_list

# Example list
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Merge the list
merged_list = merge_list(list1, list2)

print("Merged List:", merged_list)