# setdefault() - Inserts a key with a value if the key is not present
# my_dict = {'a': 1, 'b': 2}
# my_dict.setdefault('c', 3)  # Key 'c' was added
# print(my_dict)              # Output: {'a': 1, 'b': 2, 'c': 3}
# my_dict.setdefault('c', 4)  # Key 'c' already exists, so value remains 3
# print(my_dict)              # Output: {'a': 1, 'b': 2, 'c': 3}

# # update() - Updates the dictionary with key-value pairs from another dictionary
# my_dict = {'a': 1, 'b': 2}
# my_dict.update({'c': 3, 'd': 4})
# print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# # values() - Returns a view of the values
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.values())  # Output: dict_values([1, 2, 3])



# # join Two Setfs
# set1 = {'a', 'b','c',}
# set2 = {1,2,3,}

# set3 = set1.union(set2)
# print(set3)

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set1.update(set2)
# print(set1)

# # Keep ONLY the Duplicates
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection_update(y)
# print(z)

# #Keep All, But NOT the Duplicates
# x = {"cherry", "orange", "banana"}
# y = {"google", "microsoft", "apple"}

# x.symmetric_difference_update(y)
# print(x)

# x = {"cherry", "orange", "banana"}
# y = {"google", "microsoft", "apple"}

# z.symmetric_difference_update(y)
# print(z)

# #The values True and 1 Or False and 0 are considered the same value in sets, and are treated as duplicates:
# x = {"apple", "banana", "cherry", True}
# y = {"google", 1,"apple", 2}

# z = x.symmetric_difference(y)
# print(z)