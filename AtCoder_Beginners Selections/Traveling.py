N = int(input())
first_t = 0
first_x = 0
first_y = 0
ans = 'Yes'
for i in range(N):
    t, x, y = map(int, input().split())
    if abs(x - first_x) + abs(y - first_y) - t + first_t <= 0 and (abs(x - first_x) + abs(y - first_y) - t + first_t) % 2 == 0:
        first_t, first_x, first_y = t, x, y
    else:
        ans = 'No'
print(ans)