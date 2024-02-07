S = input()
T = ['eraser', 'erase', 'dreamer', 'dream']

i = 0
while i < 4:
    S = S.replace(T[i], '')
    i += 1

if len(S) == 0:
    print('YES')
else:
    print('NO')