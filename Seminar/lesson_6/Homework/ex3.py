# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Найдите самого младшего из друзей и выведите его имя.


list_friends = []
num_friends = int(input('Введите количество друзей: '))
for i in range(num_friends):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    list_friends.append(dict(name=name, age=age))

minage = min(list_friends, key=lambda x: x['age'])
print(list_friends)
print(minage['name'])