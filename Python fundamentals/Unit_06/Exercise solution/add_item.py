def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
