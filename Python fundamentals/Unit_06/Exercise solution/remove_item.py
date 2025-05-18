def remove_item(lst, item):
    new_list = lst.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
