N = int(input())
omochi_list = []
count = 0

for i in range(N):
    omochi_list.append(int(input()))

for i in range(N):
    judge = True
    for j in range(i):
        if omochi_list[j] == omochi_list[i]:
            judge = False
    if judge:
        count += 1

print(count)