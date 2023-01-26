# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def coding(s):
 
    coding = " " 
    i = 0

    while i < len(s):
        count = 1
        
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        coding += str(count) + s[i]
        i += 1
    return coding
 
        
def decoding(x):

    number = ''
    res = ''

    for i in range(len(x)):

        if not x[i].isalpha():
            number += x[i]

        else:
            res = res + x[i] * int(number)
            number = ''
            
    return res


s = 'SSSSSDDDDFFREEEWWWHHHJ'
print(coding(s))

x = '5S4D2F1R3E3W3H1J'
print(decoding(x))