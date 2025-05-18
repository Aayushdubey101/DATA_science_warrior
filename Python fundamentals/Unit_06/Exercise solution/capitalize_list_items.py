def capitalize_list_items(lst):
    capitalized_list = []
    for item in lst:
        if isinstance(item, str):
            capitalized_list.append(item.capitalize())
        else:
            capitalized_list.append(item)
    return capitalized_list

print(capitalize_list_items(['python', 'javascript', 'java', 'c++']))
print(capitalize_list_items(['apple', 'banana', 'cherry']))
