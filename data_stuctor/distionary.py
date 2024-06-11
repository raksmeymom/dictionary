# # product = {
# #     "id": 1,
# #     "name": "Laptop",
# #     "price": 1000,
# #     "quantity": 5,
# #     "description": "This is a laptop product",
# #     "color": ["black", "white", "red"],
# #     "location": (11.55738593579, 104.69439629794)
# # }

# # print(product["name"])
# # print(product["quantity"])
# # print(product["color"][1])



# product_original= {
#     "id": 1,
#     "name": "Laptop",
#     "price": 1000,
#     "quantity": 5,
#     "description": "This is a laptop product",
#     "color": ["black", "white", "red"],
#     "location": (11.55738593579, 104.69439629794)
# }


# product_copy = product_original.copy() 
# product_copy["name"] = "New Laptop"

# key = ('x','y','z')
# new_dict = dict.fromkeys(key, "value")
# bar_code = ("12233","43233","44233")
# products = dict.fromkeys(bar_code,product_original)
# list_products = products.items()
# for key, value in list_products:
#     print(f"Product:{key}")
#     print(f"{value}")

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # clear() - Empties the dictionary
# my_dict.clear()
# print(my_dict)  # Output: {}

# # copy() - Creates a shallow copy
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict = my_dict.copy()
# print(new_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# # fromkeys() - Creates a new dictionary with specified keys and values
# keys = ('x', 'y', 'z')
# value = 0
# new_dict = dict.fromkeys(keys, value)
# print(new_dict)  # Output: {'x': 0, 'y': 0, 'z': 0}



# # get() - Retrieves the value for a key (or a default if not found)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.get('b'))    # Output: 2
# print(my_dict.get('d', 0)) # Output: 0 (default value since 'd' is not a key)

# # items() - Returns a view of key-value pairs
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# # keys() - Returns a view of the keys
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])




# # pop() - Removes and returns the value associated with the specified key
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# popped_value = my_dict.pop('b')
# print(popped_value)  # Output: 2
# print(my_dict)        # Output: {'a': 1, 'c': 3}

# # popitem() - Removes and returns last inserted key-value pair (as a tuple)
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# popped_item = my_dict.popitem()
# print(popped_item)  # Output: ('c', 3)
# print(my_dict)       # Output: {'a': 1, 'b': 2} (or the remaining items)


# product_original= {
#     "id": 1,
#     "name": "Laptop",
#     "price": 1000,
#     "quantity": 5,
#     "description": "This is a laptop product",
#     "color": ["black", "white", "red"],
#     "location": (11.55738593579, 104.69439629794)
# }
# print(product.get("tax", 0)) # Output:

# text = "This is the latest laptop in the market. This laptop is very fast and good for gaming. This laptop is very expensive."

# words =  text.split(" ")
# words_count = {
  
# }

# for word in words:
#     key = word.lower()
#     words_count[key] = words_count.get(key, 0) + 1
# print(words_count)




product = {
     "id": 1,
    "name": "Laptop",
    "price": 1000,
    "quantity": 5,
    "description": "This is a laptop product",
    "color": ["black", "white", "red"],
    "location": (11.55738593579, 104.69439629794)
}

# for key, value in product.items():
#     print(f"{key}: {value}")

# trash_list = []
# poped_item = product.pop("name")
# print(poped_item)
# trash_list.append(poped_item)

# print(product)
# print(trash_list)


# trash_list_values = []
# trash_list_keys = []
# poped_item = product.pop("name")
# trash_list_keys.append("name")
# trash_list_values.append(poped_item)

# poped_item = product.pop("color")
# trash_list_keys.append("color")
# trash_list_values.append(poped_item)

# print(product)

# print(trash_list_keys)
# print(trash_list_values)

# for index in range(len(trash_list_keys)) :

#     product[trash_list_keys[index]] = trash_list_values[index]

#     print(product)

product = {
     "id": 1,
    "name": "Laptop",
    "price": 1000,
    "quantity": 5,
    "description": "This is a laptop product",
    "color": ["black", "white", "red"],
    "location": (11.55738593579, 104.69439629794)
}
product.setdefault("tax",0.1)
product.setdefault("tax",0.2)
print(product)
