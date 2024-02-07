str = input()
count = 0

for i in range(len(str)):
    if int(str[i]) == 1:
        count += 1

print(count)