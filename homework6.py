my_dict = {'Vasya': 2005, 'Egor': 1999, 'Masha': 2002}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Masha'])
print('Not existing value: ', my_dict.get('Denis'))
my_dict.update({ 'Kamila': 1981, 'Artem': 1915,})
del my_dict['Egor']
print('Modified dictionary:  ', my_dict)
print()

my_set = {1, 2, 3, 3, 3, 4, 55, 4, 'apple', 3.14159}
print('Set: ', my_set)
my_set.add(33)
my_set.add(22)
my_set.discard(3.14159)
print('Modified set:', my_set)