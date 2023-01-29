count = int(input())
translate_dict = {}
for _ in range(count):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
eng_word = input('Введите слово для перевода: ')
if translate_dict.get(eng_word):
    print(', '.join(translate_dict.get(eng_word)))
else:
    print('Такого слова нет')