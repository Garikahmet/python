# Программа получает на вход слово на английском языке и несколько его переводов на русском языке. Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. 

list_english = []
num_words = int(input('Введите количество слов: '))
for i in range(num_words):
    english_word = input('Введите слово на англ: ')
    translete = (input('перевод слова: '))
    list_english.append(dict(english_word=english_word, translete=translete.split()))
    

print(list_english)