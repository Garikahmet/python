# Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

list_fruits = []
num_fruits = int(input('Введите количество фруктов: '))
for i in range(num_fruits):
    name_fruit = input('Введите название фрукта: ')
    num_fruit = int(input('Введите количество этого фрукта: '))
    list_fruits.append(dict(name_fruit = name_fruit, num_fruit = num_fruit))

print(list_fruits)