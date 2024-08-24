my_dict = {'John': 1987, 'Gretta': 2001, 'Ragnar': 987}

print(my_dict)

# Вывыод по существующему ключу:
print(my_dict['Ragnar'])

# Вывыод по несуществующему ключу:
print(my_dict.get('William'))


my_dict.update({'Richard': 1078,
                'Carl': 1245})
print(my_dict)

tempo = my_dict.pop('John')
print(my_dict, '\n' , tempo)

my_set = {2, 4, 's', 's', 3.5, 7.9, 6, 1, 2, 3, 4, 5}

print(my_set)

my_set.add(8)
my_set.add(9)
my_set.update('t','y')
print(my_set)