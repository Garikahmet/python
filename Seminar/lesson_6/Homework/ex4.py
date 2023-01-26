# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.


name = []
age = 0
num_friends = int(input('Введите количество друзей: '))
for i in range(num_friends):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    name.append()
    age += int(age)
for b in name:
    print(max(name, key=len))
    
avg_age = age / num_friends

print(avg_age)

