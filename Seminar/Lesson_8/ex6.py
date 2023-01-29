N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
big_dict = {'name': [], 'age': []}
for el in dict_list:
    big_dict['name'].append(el['name'])
    big_dict['age'].append(el['age'])
print(big_dict)
print(big_dict.values())