

N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
summa = 0
max_name = dict_list[0]['name']
for i in dict_list:
    summa += i['age']
    if len(i['name']) > len(max_name):
        max_name = i['name']
print(summa / N)
print(max_name)