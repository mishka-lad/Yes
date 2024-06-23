my_dict = {'Михаил': 22, 'Анастасия': 32}
print(my_dict)
print(my_dict['Михаил'])
print(my_dict.get('Даша'))
my_dict.update({'Маша': 32, 'Саша': 75})
del my_dict['Михаил']
print(my_dict)

my_set = {1, 2, 3, 4, 12, 1, 12, 10, 10, 'Курва', 'бобр'}
print(my_set)
my_set.update({5, 'ёжик'})
my_set.discard('Курва')
print(my_set)