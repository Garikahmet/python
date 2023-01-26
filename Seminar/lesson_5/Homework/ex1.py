# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_list = ['арбуз', 'кот', 'енот', 'собака', 'вода', 'абвгдейка', 'страабвкпвап']
new_list = filter(lambda word: 'абв' not in word, some_list)
print(list(new_list))

