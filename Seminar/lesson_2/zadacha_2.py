# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n+1

N = int(input())
print('Для N =', N, ': {', end = ' ')
for i in range(1, N):
    print(i,': ', 3 * i + 1, end = ', ')
print(' ', N, end = '}')



# N = int(input())
# out_dict = {}
# for i in range(1, N + 1):
#   out_dict[i] = 3 * i + 1
# print(out_dict)