N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
min_age = dict_list[0]['age']
for some_dict in dict_list:
    if some_dict['age'] < min_age:
        min_age = some_dict['age']
for some_dict in dict_list:
    if some_dict['age'] == min_age:
        print(some_dict['name'])
        break